# PokeApi Pyton Connector

Python script connector *GET* to Pokemon API.

    Python Script to generate JSON file with the information stored of all pokemons

!["Pokemon Logo"](img/pokemon_logo.png)

## Test your env and script

Some scripts were made to test the requirements, python version and also the connection to the API used in this project.

```shell
pytest tests/
```
or
```shell
python -m pytest tests/
```

---

Also, to test the requirements are indeed in your enviroment, you can run the tox command

```shell
tox
```

Please remind that before running the tox command, you need to install `tox`:

```shell
pip install tox
```

## On the other hand

You can automate the execution of the python file by using 

### Use MAKE GNU

Through the following command, after having installed **MAKE GNU** into your computer, you can automate the scripting of this python file.

```shell
make pokeapi-json
```