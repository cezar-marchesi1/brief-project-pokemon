# Pokemon API Challenge

This project consists of Flask application with two endpoints to fetch data from [the pokemon api](https://pokeapi.co/).

## 1. Endpoints

### **API Service Endpoints**


#### **POST /process_pokemons** - Fetch pokemon data from source and process it
- **Description**: Receives in the body of the request a list with the names of the pokemons that must be fetched.
- **Example Payload**:

```json
{
    "pokemon_names": ["charizard", "pikachu", "squirtle", "gengar"]
}
```

- **Example Response**:

```json
{
    "message": "Pokémons processed successfully."
}
  ```
<hr/> 

#### **GET  /pokemons** - Show processed pokemons
- **Description**: Lists all the pokemon data saved in our database. 
- **Example Response**:
```json
  {
    [
        {
            "abilities": [
                "static",
                "lightning-rod"
            ],
            "base_experience": 112,
            "height": 4,
            "id": 1,
            "name": "pikachu",
            "types": [
                "electric"
            ],
            "weight": 60
        }
    ]
  }
```

<hr/>

## 2. Running the Services

#### The configuration of the service is made with a .env file that must contain the URL for the PokeAPI and the URI for the database. There is a .env_example file that can be used as a base.

To run the service we use docker. From the root of the project, execute the following:

#### `docker build -t my-app .`


#### `docker run -p 5000:5000 my-app`


Make sure Docker is installed and running on your machine before executing these commands.

<hr/>

## 3. Tests

#### There are tests covering our routes, the domain and the service. You can execute the tests by opening a shell in the app container and running the command `pytest`.


<hr/>
