"""Tests for the VibeGen class."""

from unittest.mock import Mock, patch

import pytest

from vibegen.config.config import VibeGenConfig
from vibegen.utils.logger import console_logger
from vibegen.vibegen import VibeGen


@pytest.fixture
def mock_vibe_llm_client():
    """Fixture to mock the VibeLlmClient."""
    with patch("vibegen.vibegen.VibeLlmClient") as mock_client:
        yield mock_client


def test_vibegen_init(mock_vibe_llm_client: Mock):
    """Test the __init__ method of VibeGen."""
    mock_llm_instance = Mock()
    mock_vibe_llm_client.return_value = mock_llm_instance

    client = Mock()
    model = "test-model"
    config = VibeGenConfig()

    vibe_check = VibeGen(client, model, config=config)

    mock_vibe_llm_client.assert_called_once_with(
        client, model, config, console_logger
    )
    assert vibe_check.llm is mock_llm_instance


def test_vibegen_init_with_dict_config(mock_vibe_llm_client: Mock):
    """Test the __init__ method of VibeGen with a dict config."""
    mock_llm_instance = Mock()
    mock_vibe_llm_client.return_value = mock_llm_instance

    client = Mock()
    model = "test-model"
    config_dict = {"timeout": 5000}

    vibe_check = VibeGen(client, model, config=config_dict)

    assert mock_vibe_llm_client.call_args[0][0] is client
    assert mock_vibe_llm_client.call_args[0][1] == model
    assert isinstance(mock_vibe_llm_client.call_args[0][2], VibeGenConfig)
    assert mock_vibe_llm_client.call_args[0][2].timeout == 5000
    assert mock_vibe_llm_client.call_args[0][3] is console_logger
    assert vibe_check.llm is mock_llm_instance


def test_vibegen_call_with_return_type(mock_vibe_llm_client: Mock):
    """Test the __call__ method of VibeGen with a return type."""
    mock_llm_instance = Mock()
    mock_llm_instance.vibe_eval.return_value = "mocked response"
    mock_vibe_llm_client.return_value = mock_llm_instance

    client = Mock()
    model = "test-model"
    vibe_gen = VibeGen(client, model)

    @vibe_gen
    def my_function(a: int, b: str) -> str:
        """My function docstring."""
        pass

    result = my_function(1, b="2")

    assert result == "mocked response"
    mock_llm_instance.vibe_eval.assert_called_once()
    prompt = mock_llm_instance.vibe_eval.call_args[0][0]
    return_type = mock_llm_instance.vibe_eval.call_args[0][1]

    assert "my_function(a: int, b: str) -> str" in prompt
    assert "My function docstring." in prompt
    assert "Arguments: (1,), {'b': '2'}" in prompt
    assert return_type is str


def test_vibegen_call_with_no_return_type(mock_vibe_llm_client: Mock):
    """Test the __call__ method of VibeGen with no return type."""
    mock_llm_instance = Mock()
    mock_llm_instance.vibe_eval.return_value = "mocked response"
    mock_vibe_llm_client.return_value = mock_llm_instance

    client = Mock()
    model = "test-model"
    vibe_gen = VibeGen(client, model)

    @vibe_gen
    def my_function(a: int, b: str):
        """My function docstring."""
        pass

    result = my_function(1, b="2")

    assert result == "mocked response"
    mock_llm_instance.vibe_eval.assert_called_once()
    prompt = mock_llm_instance.vibe_eval.call_args[0][0]
    return_type = mock_llm_instance.vibe_eval.call_args[0][1]
    
    assert "my_function(a: int, b: str)" in prompt
    assert "My function docstring." in prompt
    assert "Arguments: (1,), {'b': '2'}" in prompt
    assert return_type is str