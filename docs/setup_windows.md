# Getting Started on Windows

This guide will walk you through setting up the project on a Windows machine using PowerShell.

### 1. Install Requirements

You will need to install Python and Git.

- Python 3.10+  
- Git

### 2. Clone the Repository

Open PowerShell and run the following commands to clone the project and navigate into the directory.

```powershell
git clone https://github.com/davidheeren/IrrigationEducatorAgent.git
cd IrrigationEducatorAgent
```

### 3. Create and Activate Virtual Environment

A virtual environment keeps your project's dependencies separate.

```powershell
# Create the virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate
```
> **Note:** You will need to run the `activate` command again if you open a new terminal.

### 4. Install Dependencies

Install the required Python packages with pip.

```powershell
pip install -r requirements.txt
```

### 5. Add API Key

1.  Open a text editor (like Notepad).
2.  Create a new file.
3.  Paste the following line into the file, replacing `your-openai-api-key-here` with your actual key:
    ```
    OPENAI_API_KEY=your-openai-api-key-here
    ```
4.  Save the file in the `IrrigationEducatorAgent` project directory with the name `.env`. Make sure it is not saved as `.env.txt`.
