.PHONY: pokeapi-json
pokeapi-json:
	@echo "Starting request..."
	@python getrequest.py && echo "\nProcess completed... check result folder"