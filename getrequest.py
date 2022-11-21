import sys, os, json
import requests

class PokeAPI():
    """
    Methods
    ---
    """
    def __init__(self, pokemons:int=300):
        """
        Class initialized by the following function
        Params: pokemons ([Not Required] int, default = 300)
        Objective: Establish params for request
        """
        print("Creating PokeAPI object...\n")       
        self.data = []
        self.url = "https://pokeapi.co/api/v2/pokemon/{}/"
        self.pokemons = pokemons
        self.params = {'limit': self.pokemons}
    def establish_connection(self):
        """
        Class Method
        Params: No parameters/arguments
        Objective: Establish connection and execute request
        """
        try:
            for number in range(1, self.pokemons):
                print("Starting request to URL: {}\n".format(self.url.format(number)))
                self.params['offset'] = number
                response = requests.get(url=self.url.format(number), params=self.params)
                if response.status_code != 200: 
                    print(response.text)
                else:
                    data = response.json()
                    print(data["name"])
                    self.data.append(data)
        except Exception as error:
            print("ERROR: {}".format(error))
    def read_file_pokeapi(self):
        """
        Class Method
        Params: No parameters/arguments
        Objective: Save data into JSON file
        """
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            self.filename = dir_path + "\\result\\pokeapi.json"
            print(self.filename)
            with open(self.filename, "w") as file:
                json_object = json.dumps(self.data, indent=4)
                file.write(json_object)
            return True
        except Exception as error:
            print("ERROR: {}".format(error))
            return False

if __name__ == "__main__":
    print("\n---")
    buff = PokeAPI()
    buff.establish_connection()
    read = buff.read_file_pokeapi()
    if(read == True):
        sys.exit(0)
    else:
        print("ERROR encountered... File reading")
        sys.exit(1)