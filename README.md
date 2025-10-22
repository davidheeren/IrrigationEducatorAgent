# Irrigation Educator Agent

The **Irrigation Educator Agent** is a terminal-based AI assistant designed to support irrigation education and decision-making in Nebraska and beyond. It provides plain-language explanations, practical recommendations, and guided support for students, educators, and agricultural producers.

## Features

- Conversational AI agent powered by OpenAI
- Tailors responses based on user type (e.g., student, farmer)
- Pulls information from primary and secondary irrigation documents
- Provides example calculations and explains irrigation management concepts
- Supports file search and web search tools

## Getting Started

### Requirements

- Python 3.10+
- git
- (Optional) Virtual environment
- Look in requirements.txt

### Installation

1. Clone the repo:

    **powershell or bash**
    ```bash
    git clone https://github.com/davidheeren/IrrigationEducatorAgent.git
    cd IrrigationEducatorAgent
    ```

2. Create and activate a virtual environment:

    **powershell**
    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    ```

    **bash**
    ```bash
    python -m venv .venv
    source .venv/bin/activate 
    ```

3. Install dependencies:

    **powershell or bash**
    ```bash
    pip install -r requirements.txt
    ```

4. Create API key file:

    **powershell**
    ```powershell
    New-Item .env -Value "OPENAI_API_KEY=your-openai-api-key-here"
    ```

    **bash**
    ```bash 
    echo "OPENAI_API_KEY=your-openai-api-key-here" > .env
    ```


### Run the Agent

1. Run

    **powershell or bash**
    ```bash
    python main.py
    ```

## Configuration

The agent is configured via JSON in `config/agent_config.json`.  
You can enable or disable tools such as:

- GPT api settings
- File search
- Web search
- Custom functions

## Usage

- Type 'q' to quit

## Notes

- This agent uses the OpenAI Assistants API and requires an API key.
- **Markdown formatting** is supported in responses.
