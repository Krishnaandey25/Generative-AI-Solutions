import pytest
from src.main import LLMOrchestrator, OpenAIProvider, AnthropicProvider

def test_orchestrator_factory():
    \"\"\"Test LLMOrchestrator factory method creates correct provider.\"\"\"
    orchestrator = LLMOrchestrator.create(provider_type="openai")
    assert isinstance(orchestrator.provider, OpenAIProvider)
    
    orchestrator = LLMOrchestrator.create(provider_type="anthropic")
    assert isinstance(orchestrator.provider, AnthropicProvider)

def test_orchestrator_context_manager():
    \"\"\"Test LLMOrchestrator context manager functionality.\"\"\"
    with LLMOrchestrator.create(provider_type="openai") as orchestrator:
        response = orchestrator.execute_request("Test prompt")
        assert "[OpenAI]" in response
        assert "Test prompt" in response
