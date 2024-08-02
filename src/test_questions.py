from pathlib import Path
from helpers import get_response_content, system_template, questions_and_expected
from testcontainers.ollama import OllamaContainer

MODEL_NAME = "llama3:latest"

def test_llm_responses():
    with OllamaContainer(ollama_home=Path.home() / ".ollama") as ollama:
        if MODEL_NAME not in [e["name"] for e in ollama.list_models()]:
            print(f"Did not find {MODEL_NAME}, pulling")
            ollama.pull_model(MODEL_NAME)
        endpoint = ollama.get_endpoint()
        
        for question, expected_name in questions_and_expected:
            response_content = get_response_content(endpoint, MODEL_NAME, system_template, question)
            print(f"User question: {question}")
            print(f"Response: {response_content}")
            assert expected_name in response_content, f"Expected '{expected_name}' in the response, but got: {response_content}"

if __name__ == "__main__":
    test_llm_responses()
