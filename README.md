# LLM Testing with Testcontainers and Ollama

## Introduction

This project demonstrates how to test Large Language Models (LLMs) and prompts using Testcontainers and Ollama in Python. This setup provides a robust and repeatable testing environment to ensure your LLM behaves as expected under various conditions.

## Prerequisites

To run this project, you'll need:

- Python 3.8 or higher
- Docker (version 20.10 or higher)
- Basic knowledge of Python programming
- Familiarity with `pytest` is helpful

## Project Structure
```plaintext
tc-python-ollama/
├── src/
│   ├── __init__.py
│   ├── helpers.py
│   ├── test_questions.py
├── requirements.txt
├── README.md
```


## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/bricefotzo/tc-python-ollama.git
    cd tc-python-ollama
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```bash
    virtualenv .venv
    source .venv/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Tests

1. **Navigate to the `src` directory:**
    ```bash
    cd src
    ```

2. **Run the tests using pytest:**
    ```bash
    pytest test_questions.py
    ```

This will spin up the Ollama container, run the defined tests, and print the results.

> Don't hesitate to explore the code and experiment with different prompts and test cases to see how the LLM behaves in various scenarios.

I'm open to feedback and suggestions for improving this project. Feel free to reach out with any questions or ideas!