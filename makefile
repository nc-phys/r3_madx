PROJECT_NAME = r3_madx
VENV_DIR = .env

.PHONY: all
all: help

.PHONY: help
help:
	@echo "  init - Create a Python environment and install requirements"

.PHONY: init
init:
	@if [ ! -d $(VENV_DIR) ]; then \
		echo "Creating Python environment in $(VENV_DIR)..."; \
		python3 -m venv $(VENV_DIR); \
		sed -i.bak 's|PS1="(.env)|PS1="($(PROJECT_NAME))|' $(VENV_DIR)/bin/activate; \
		$(VENV_DIR)/bin/pip install --upgrade pip; \
		echo "Installing requirements from requirements.txt..."; \
		$(VENV_DIR)/bin/pip install -r requirements.txt; \
		echo "Python environment created and requirements installed."; \
		echo "Activate environment using command \"source .env/bin/activate\""; \
	else \
		echo "Python environment already exists in $(VENV_DIR)."; \
	fi
