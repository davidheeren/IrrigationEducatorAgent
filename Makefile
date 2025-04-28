VENV_DIR = .venv

setup:
	@echo "Creating virtual environment..."
	python -m venv $(VENV_DIR)
	@echo "Installing dependencies..."
	$(VENV_DIR)/Scripts/pip install -r requirements.txt

run: $(VENV_DIR)/Scripts/activate
	@echo "Running main script..."
	@$(VENV_DIR)/Scripts/python scripts\main.py
# @echo -e "\n"

help:
	@echo "Makefile commands:"
	@echo "  make setup      - Create virtual environment and install dependencies"
	@echo "  make run        - Run the main Python script"
