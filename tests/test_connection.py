import pytest
def test_build():
    """
    Python pytest function
    Params: No parameters/arguments
    Objective: Checks if the hardcoded values has been installed into the env.
    """
    import requests
    url = "https://pokeapi.co/api/v2/pokemon/{}/"
    number = 1
    params = {'limit': number}
    print("Starting request to URL: {}\n".format(url.format(number)))
    params['offset'] = number
    response = requests.get(url=url.format(number), params=params)
    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        print(data["name"])
        data.append(data)