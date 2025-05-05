VENV_DIR = .venv

all: help

setup:
	@echo "Creating virtual environment..."
	python -m venv $(VENV_DIR)
	@echo "Installing dependencies..."
	$(VENV_DIR)/Scripts/pip install -r requirements.txt
	@echo "OPENAI_API_KEY=your-openai-api-key-here" > .env
	@echo "Enter your api key in the '.env' file"

run: $(VENV_DIR)/Scripts/activate
	@echo "Running main script..."
	@$(VENV_DIR)/Scripts/python main.py
# @echo -e "\n"

help:
	@echo "Makefile commands:"
	@echo "  make setup      - Create virtual environment and install dependencies"
	@echo "  make run        - Run the main Python script"
