<p align="center">
  <img width="220px" src="https://raw.githubusercontent.com/vibe-engineers/vibegen/main/assets/vibegen.png" />
  <h1 align="center">VibeGen Developer Guide</h1>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Navigating this Developer Guide](#navigating-this-developer-guide)
* [Setup](#setup)
* [Project Structure](#project-structure)
* [Key Concepts & Design](#key-concepts--design)
* [Code Documentation](#code-documentation)
* [Testing](#testing)
* [Pull Requests](#pull-requests)
* [Final Notes](#final-notes)

<div style="page-break-after: always;"></div>

## Introduction

For a product overview, start with the project [*README*](../README.md) and the public [*wiki*](https://github.com/vibe-engineers/vibegen/wiki). This developer guide assumes familiarity with modern Python packaging (virtual environments, pip) and basic Large Language Model (LLM) usage. The goal here is to help you move quickly inside a compact codebase without being overwhelmed by ceremony.

## Navigating this Developer Guide

We keep the syntax cues simple so you can skim effectively:

| Syntax     | Description                                      |
| ---------- | ------------------------------------------------ |
| `Markdown` | Commands or code snippets (e.g. `hatch run test`) |
| *Italics*  | Files or folders (e.g. *src/vibegen*)             |
| **Bold**   | Concepts to pay attention to                     |

<div style="page-break-after: always;"></div>

## Setup

VibeGen targets Python 3.0+ and ships on PyPI. To work on the project locally:

1. Fork and clone the repository.
   ```bash
   git clone https://github.com/<your-user>/vibegen.git
   cd vibegen
   ```
2. Create and activate a virtual environment (any tool works — `venv`, `uv`, `conda`).
3. Install dependencies for development.
   ```bash
   python -m pip install -r requirements.txt -r requirements-dev.txt
   ```
4. If you intend to exercise live LLM calls, copy the `.env.template` to create the `.env` file and fill in provider credentials (e.g. `OPENAI_API_KEY`, `GEMINI_API_KEY`).
5. Run the unit tests once to verify the environment.
   ```bash
   hatch run test
   ```

That is enough to iterate on the library. When you want to try VibeGen inside another project, use the editable install:
```bash
python -m pip install -e .
```

## Project Structure

VibeGen keeps a lean layout so the moving parts are easy to reason about:

- *src/vibegen*: Python package published to PyPI.
  - *vibegen.py*: Home of the **VibeGen** decorator/facade that developers wrap functions with.
  - *config/config.py*: Declarative knobs built on top of `vibetools.VibeConfig`, including the default system instruction.
  - *utils/logger.py*: Central console logger used across the package for consistent output.
- *tests*: Pytest suite for the exported surface area plus helpers under *tests/utils*.
- *examples*: Minimal usage samples.
- *docs/DeveloperGuide.md*: This document.

External dependencies such as `VibeLlmClient`, `VibeConfig`, and logging primitives live in the sibling [**vibetools**](https://github.com/vibe-engineers/vibetools) package. The code here focuses on tailoring those primitives into the developer-friendly interface that ships as `vibegen`.

## Key Concepts & Design

Although the library is compact, a couple of patterns are worth knowing before you add features:

### VibeGen decorator

`VibeGen` wraps an underlying `VibeLlmClient`. The constructor normalises incoming configuration by accepting a `VibeGenConfig`, a plain dictionary, or nothing at all. When used as a decorator, the wrapper inspects the target function’s signature and docstring to build a prompt, then delegates to `vibe_eval`. Keep the API predictable and side-effect free: pass a callable and receive the mocked return value produced by the backing LLM.

### Configuration defaults

`VibeGenConfig` subclasses `VibeConfig` to seed a default `system_instruction`. This keeps inference prompts consistent while still allowing advanced users to override options like retry counts, timeouts, or temperature. When adding new configuration toggles, prefer extending `VibeGenConfig` so downstream users inherit sane defaults.

### Prompt fidelity & type enforcement

The decorator captures positional and keyword arguments, the declared return annotation, and the docstring to ensure the prompt gives the LLM all necessary context. If a function omits a return type, the wrapper falls back to `str` to keep responses predictable. Changes here should preserve compatibility with existing prompts and maintain strict return-type enforcement.

### Logging

`utils.console_logger` provides the only logging surface that library code should touch. This keeps stdout noise minimal and allows the hosting application to redirect or silence messages in one spot. If additional logging is required, expose it through this logger instead of creating new loggers.

### Testing boundaries

Tests assert behaviours at the package boundary. Integration with remote models is faked through mocks and stubs in *tests* so the suite runs quickly and deterministically. When contributing new features, extend the mocks rather than talking to live APIs.

## Code Documentation

Keep docstrings and inline comments short but purposeful:

- Every public module, class, and function should have a brief docstring summarising intent.
- Use Google-style docstrings to align with `darglint` checks.
- Add inline comments sparingly for non-obvious logic or TODOs (`# todo: investigate retry jitter`).

Consistent documentation keeps linting green (`hatch run lint`) and lowers the barrier for new contributors.

## Testing

Quality gates are lightweight and fast:

- `hatch run lint` → Runs `darglint`, `ruff`, and `black --check` over *src*.
- `hatch run test` → Executes the pytest suite under *tests*.

Run both before opening a pull request. If you touch packaging metadata, also sanity-check distribution builds with `hatch build`.

## Pull Requests

We favour small, well-scoped changes with clear intent:

1. Branch from `main` in your fork and keep the commit history tidy.
2. Update documentation or examples whenever you change public behaviour.
3. Fill in the pull request template, including screenshots or logs when relevant.
4. Tag reviewers if the change affects external APIs or published packages.

Discuss larger roadmap items in an issue or on [Discord](https://discord.gg/dBW35GBCPZ) before investing significant effort.

## Final Notes

This guide will evolve with the codebase. If you spot gaps or outdated advice, open a quick pull request to fix it — documentation is part of the product. Happy vibing!
