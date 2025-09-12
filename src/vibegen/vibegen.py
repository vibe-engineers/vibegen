"""The main VibeGen class and its functionalities."""

import inspect
from typing import Any, Callable

from vibetools._internal import VibeLlmClient

from vibegen.config.config import VibeGenConfig
from vibegen.utils.logger import console_logger


class VibeGen:
    """
    A class that uses LLMs to perform "vibe generate" on functions.

    This class can be used as a decorator to evaluate the outcome of a function call.
    """

    def __init__(
        self,
        client: VibeLlmClient,
        model: str,
        *,
        config: VibeGenConfig | dict | None = None,
    ) -> None:
        """
        Initialize the VibeGen object.

        Args:
            client: An instance of VibeLlmClient.
            model: The name of the model to use for the LLM.
            config: VibeGenConfig containing runtime knobs (e.g., num_tries).

        """
        if config is None:
            config = VibeGenConfig()
        elif isinstance(config, dict):
            config = VibeGenConfig(**config)

        self.llm = VibeLlmClient(client, model, config, console_logger)

    def __call__(self, arg: Callable[..., Any]) -> Callable[..., Any]:
        """
        Perform a vibe generate on a function.

        Args:
            arg: A function to evaluate.

        Returns:
            The evaluated output of the function.

        """

        def wrapper(*args, **kwargs):
            signature = inspect.signature(arg)
            func_signature = f"{arg.__name__}{str(signature)}"
            docstring = inspect.getdoc(arg)
            prompt = f"""
            Function Signature: {func_signature}
            Docstring: {docstring}
            Arguments: {args}, {kwargs}
            """
            return_type = signature.return_annotation
            if return_type is inspect.Signature.empty:
                return_type = str
            return self.llm.vibe_eval(prompt, return_type)

        return wrapper
