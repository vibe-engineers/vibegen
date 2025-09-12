<p align="center">
  <h1 align="center">VibeGen</h1>
</p>

<p align="center">
  <a href="https://github.com/vibe-engineers/vibegen/actions/workflows/ci-cd-pipeline.yml"> <img src="https://github.com/vibe-engineers/vibegen/actions/workflows/ci-cd-pipeline.yml/badge.svg" /> </a>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Team](#team)
* [Contributing](#contributing)
* [Others](#others)

### Introduction
**VibeGen** is a lightweight python package that allows users to use natural language (LLMs) to generate responses for functions that are described but not implemented. It acts as a decorator that intercepts function calls and uses an LLM to generate a plausible return value based on the function's signature and docstring.

It supports OpenAI and Google Gemini clients currently, and a simple example illustrating how it can be used is shown below:
```python
from google import genai
from vibegen import VibeGen

# initialize client
client = genai.Client(api_key=GEMINI_API_KEY)

# wrap it in VibeGen
vg = VibeGen(client, model="gemini-2.0-flash-lite")

@vg
def get_antonym(word: str) -> str:
    """
    This function takes a word and returns its antonym.
    For example, the antonym of 'hot' is 'cold'.
    """
    pass

# a simple example that gets the antonym of a word
user_input = input("Enter a word:")
antonym = get_antonym(user_input)
print(f"The antonym of {user_input} is {antonym}")
```

**VibeGen** is published on [**pypi**](https://pypi.org/project/vibegen/) and can be easily installed with:
```bash
python3 -m pip install vibegen
```

### Features
- **Function Mocking**: Automatically generate responses for functions that are described but not yet implemented.
- **Natural Language Implementation**: Use docstrings to define the behavior of your functions in natural language.
- **Multi-provider Support**: Seamlessly switch between different LLM providers. VibeGen currently supports OpenAI and Google Gemini.
- **Type Hint Enforcement**: Ensures that the generated response strictly matches the declared return type of the function.

### Technologies
Technologies used by VibeGen are as below:
##### Done with:

<p align="center">
  <img height="150" width="150" src="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"/>
</p>
<p align="center">
Python
</p>

##### Project Repository
```
https://github.com/vibe-engineers/vibegen
```

### Team
* [Kong Le-Yi](https://github.com/konglyyy)
* [Tan Jin](https://github.com/tjtanjin)

### Contributing
If you are looking to contribute to the project, you may find the [**Developer Guide**](https://github.com/vibe-engineers/vibegen/blob/main/docs/DeveloperGuide.md) useful.

In general, the forking workflow is encouraged and you may open a pull request with clear descriptions on the changes and what they are intended to do (enhancement, bug fixes etc). Alternatively, you may simply raise bugs or suggestions by opening an [**issue**](https://github.com/vibe-engineers/vibegen/issues) or raising it up on [**discord**](https://discord.gg/dBW35GBCPZ).

Note: Templates have been created for pull requests and issues to guide you in the process.

### Others
For any questions regarding the implementation of the project, you may also reach out on [**discord**](https://discord.gg/dBW35GBCPZ).
