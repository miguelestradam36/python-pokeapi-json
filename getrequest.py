from pokemon.pokerequest import PokeAPI

if __name__ == "__main__":
    print("\n---")
    buff = PokeAPI(pokemons=10)
    buff.establish_connection()
    read = buff.file_pokeapi()
    if read:
        print("Information saved into JSON file...")
    else:
        print("There was an error with the request to the Pokemon API...")
        raise Exception("ERROR")