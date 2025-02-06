class PokeAPI():
    """
    Attributes
    ---
    """
    json_ = __import__("json")
    sys_ = __import__("sys")
    os_ = __import__("os")
    requests_ = __import__("requests")

    """
    Methods
    ---
    """
    
    def __init__(self, pokemons:int=3):
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

    def establish_connection(self)->None:
        """
        Class Method
        Params: No parameters/arguments
        Objective: Establish connection and execute request
        """
        try:
            for number in range(1, self.pokemons):
                print("Starting request to URL: {}\n".format(self.url.format(number)))
                self.params['offset'] = number
                response = self.requests_.get(url=self.url.format(number), params=self.params)
                if response.status_code != 200: 
                    print(response.text)
                else:
                    data = response.json()
                    print(data["name"])
                    self.data.append(data)
        except Exception as error:
            print("ERROR: {}".format(error))

    def file_pokeapi(self)->bool:
        """
        Class Method
        Params: No parameters/arguments
        Objective: Save data into JSON file
        """
        try:
            dir_path = self.os_.path.dirname(self.os_.path.realpath(__file__))
            self.filename = self.os_.path.join(dir_path, "pokeapi.json")
            print(self.filename)
            with open(self.filename, "w") as file:
                json_object = self.json_.dumps(self.data, indent=4)
                file.write(json_object)
            return True
        except Exception as error:
            print("ERROR: {}".format(error))
            return False