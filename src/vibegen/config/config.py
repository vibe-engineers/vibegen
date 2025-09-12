"""Configuration objects for VibeGen."""

from typing import Any

from vibetools._internal import VibeConfig


class VibeGenConfig(VibeConfig):
    """
    Configuration for VibeGen, extending the base VibeConfig.

    This configuration sets a default system instruction for the LLM.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the VibeGenConfig object.

        Args:
            *args: Positional arguments to pass to the parent VibeConfig.
            **kwargs: Keyword arguments to pass to the parent VibeConfig.
                      'system_instruction' is given a default value.

        """
        kwargs.setdefault(
            "system_instruction",
            "You will be given: a function signature (name, parameters, and return type); "
            "a docstring describing what the function is intended to do; "
            "the concrete arguments passed to the function; and the declared return value type. "
            "Your task is to: "
            "(1) interpret the docstring to understand the intended behavior of the function, "
            "(2) use the provided arguments to simulate what the function would logically produce, "
            "(3) ensure your response strictly matches the declared return type, "
            "both in structure and data type, and "
            "(4) return only the value that fulfills the function’s contract, "
            "with no explanations, commentary, or extra text.",
        )

        super().__init__(*args, **kwargs)
