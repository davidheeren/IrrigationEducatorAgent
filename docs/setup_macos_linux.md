# Getting Started on macOS & Linux

This guide will walk you through setting up the project on macOS or Linux using the bash terminal.

### 1. Install Requirements

- Python 3.10+  
- Git

### 2. Clone the Repository

Open your terminal and run the following commands to clone the project and navigate into the directory.

```bash
git clone https://github.com/davidheeren/IrrigationEducatorAgent.git
cd IrrigationEducatorAgent
```

### 3. Create and Activate Virtual Environment

A virtual environment keeps your project's dependencies separate.

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages with pip.

```bash
pip install -r requirements.txt
```

### 5. Add API Key

Run the following command in your terminal, replacing `your-openai-api-key-here` with your actual key.

```bash
echo "OPENAI_API_KEY=your-openai-api-key-here" > .env
```
