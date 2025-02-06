.PHONY: pokeapi-json
pokeapi-json:
	@echo "Installing requirements..."
	@pip install -r requirements.txt
	@echo "Starting request..."
	@python getrequest.py && echo "\nProcess completed... check result folder"