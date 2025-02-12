import pytest
from pydantic import HttpUrl
from typing import Optional
from models_dto import (
    PokemonDTO, NamedAPIResource, AbilityEntry, FormEntry,
    Sprites, StatEntry, TypeEntry
)


@pytest.fixture
def sample_pokemon_dto():
    return PokemonDTO(
        id=25,
        name="Pikachu",
        base_experience=112,
        height=4,
        weight=60,
        abilities=[
            AbilityEntry(
                ability=NamedAPIResource(name="static", url=HttpUrl(
                    "https://pokeapi.co/api/v2/ability/9/")),
                is_hidden=False,
                slot=1
            ),
            AbilityEntry(
                ability=NamedAPIResource(
                    name="lightning-rod", url=HttpUrl("https://pokeapi.co/api/v2/ability/31/")),
                is_hidden=True,
                slot=3
            )
        ],
        forms=[
            FormEntry(name="pikachu", url=HttpUrl(
                "https://pokeapi.co/api/v2/pokemon-form/25/"))
        ],
        sprites=Sprites(
            front_default=HttpUrl(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"),
            back_default=HttpUrl(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png"),
            front_shiny=HttpUrl(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png"),
            back_shiny=HttpUrl(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/25.png")
        ),
        stats=[
            StatEntry(
                base_stat=35,
                effort=0,
                stat=NamedAPIResource(name="hp", url=HttpUrl(
                    "https://pokeapi.co/api/v2/stat/1/"))
            ),
            StatEntry(
                base_stat=55,
                effort=0,
                stat=NamedAPIResource(name="attack", url=HttpUrl(
                    "https://pokeapi.co/api/v2/stat/2/"))
            )
        ],
        types=[
            TypeEntry(
                slot=1,
                type=NamedAPIResource(name="electric", url=HttpUrl(
                    "https://pokeapi.co/api/v2/type/13/"))
            )
        ]
    )


class MockPokemonDTO:
    def __init__(self, name, base_experience, height, weight, abilities, types):
        self.name = name
        self.base_experience = base_experience
        self.height = height
        self.weight = weight
        self.abilities = abilities
        self.types = types


class MockPokemonDomain:
    def __init__(self, name, base_experience, height, weight, abilities, types):
        self.name = name
        self.base_experience = base_experience
        self.height = height
        self.weight = weight
        self.abilities = abilities
        self.types = types

    @classmethod
    def from_dto(cls, dto):
        return MockPokemonDomain(
            name=dto.name,
            base_experience=dto.base_experience,
            height=dto.height,
            weight=dto.weight,
            abilities=dto.abilities,
            types=dto.types
        )


@pytest.fixture
def sample_pokemon_response():
    return {
        "name": "charmander",
        "base_experience": 62,
        "height": 6,
        "weight": 85,
        "abilities": [{"ability": {"name": "blaze"}}],
        "types": [{"type": {"name": "fire"}}]
    }
