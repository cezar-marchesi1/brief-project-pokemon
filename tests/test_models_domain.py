from models_domain import PokemonDomain
from tests.fixtures import sample_pokemon_dto


def test_pokemon_domain_creation():
    pokemon = PokemonDomain(
        name="Bulbasaur", base_experience=64, height=7, weight=69)

    assert pokemon.name == "Bulbasaur"
    assert pokemon.base_experience == 64
    assert pokemon.height == 7
    assert pokemon.weight == 69
    assert pokemon.abilities == []
    assert pokemon.types == []


def test_add_ability():
    pokemon = PokemonDomain(
        name="Bulbasaur", base_experience=64, height=7, weight=69)
    pokemon.add_ability("Overgrow")

    assert "Overgrow" in pokemon.abilities


def test_add_type():
    pokemon = PokemonDomain(
        name="Bulbasaur", base_experience=64, height=7, weight=69)
    pokemon.add_type("Grass")

    assert "Grass" in pokemon.types


def test_to_dict():
    pokemon = PokemonDomain(
        name="Charmander",
        base_experience=62,
        height=6,
        weight=85,
        abilities=["Blaze"],
        types=["Fire"]
    )
    expected_dict = {
        "name": "Charmander",
        "base_experience": 62,
        "height": 6,
        "weight": 85,
        "abilities": ["Blaze"],
        "types": ["Fire"]
    }

    assert pokemon.to_dict() == expected_dict


def test_from_dto(sample_pokemon_dto):
    pokemon = PokemonDomain.from_dto(sample_pokemon_dto)

    print(pokemon.abilities)

    assert pokemon.name == "Pikachu"
    assert pokemon.base_experience == 112
    assert pokemon.height == 4
    assert pokemon.weight == 60
    assert "static" in pokemon.abilities
    assert "lightning-rod" in pokemon.abilities
    assert "electric" in pokemon.types
