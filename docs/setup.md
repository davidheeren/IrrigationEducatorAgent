# Getting Started

### Requirements

- Python 3.10+
- Python pip and venv
- Git

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

    - You have to activate the virtual environment in every new terminal session  
    - The .venv file structure depends on the operating system

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
