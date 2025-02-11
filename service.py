import config
import requests
from typing import List
from database import db
from repository import *
from models_dto import PokemonDTO
from models_domain import PokemonDomain


def fetch_and_save_pokemons(pokemon_names: List[str]) -> None:
    base_url = config.POKEMON_API

    for name in pokemon_names:
        try:
            response = requests.get(f"{base_url}{name.lower()}")
            response.raise_for_status()
            data = response.json()

            pokemon_dto = PokemonDTO(**data)
            
            pokemon_domain = PokemonDomain.from_dto(pokemon_dto)

            existing_pokemon = Pokemon.query.filter_by(
                name=pokemon_domain.name).first()
            if existing_pokemon:
                print(f"Pokémon '{pokemon_domain.name}' Already exists", flush=True)
                continue

            pokemon = Pokemon(
                name=pokemon_domain.name,
                base_experience=pokemon_domain.base_experience,
                height=pokemon_domain.height,
                weight=pokemon_domain.weight
            )

            for ability_name in pokemon_domain.abilities:
                ability = Ability(name=ability_name, pokemon=pokemon)
                pokemon.abilities.append(ability)

            for type_name in pokemon_domain.types:
                type_obj = Type.query.filter_by(name=type_name).first()
                if not type_obj:
                    type_obj = Type(name=type_name)
                pokemon.types.append(type_obj)

            db.session.add(pokemon)
            db.session.commit()

            print(f"-> Pokémon '{pokemon.name}' successfully saved!", flush=True)
            
        

        except requests.HTTPError as http_err:
            print(f"HTTP Error processing '{name}': {http_err}", flush=True)
            return name, http_err
        except Exception as err:
            print(f"Error Processing '{name}': {err}", flush=True)
            db.session.rollback()
            return name, err
    return None, None
