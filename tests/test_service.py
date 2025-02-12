import requests
from unittest.mock import patch, MagicMock
from service import fetch_and_save_pokemons
from tests.fixtures import MockPokemonDomain, MockPokemonDTO, sample_pokemon_response


@patch("requests.get")
@patch("service.db.session")
def test_fetch_and_save_pokemons(mock_db_session, mock_requests_get, sample_pokemon_response):
    mock_response = MagicMock()
    mock_response.json.return_value = sample_pokemon_response
    mock_response.raise_for_status.return_value = None
    mock_requests_get.return_value = mock_response

    mock_pokemon_query = MagicMock()
    mock_pokemon_query.filter_by.return_value.first.return_value = None

    with patch("service.PokemonDTO", new=MockPokemonDTO), \
            patch("service.PokemonDomain", new=MockPokemonDomain), \
            patch("repository.Pokemon.query", new=mock_pokemon_query):

        fetch_and_save_pokemons(["Charmander"])

    assert mock_requests_get.called
    mock_db_session.add.assert_called()
    mock_db_session.commit.assert_called()


@patch("requests.get")
def test_fetch_and_save_pokemons_http_error(mock_requests_get):
    mock_requests_get.side_effect = requests.HTTPError("404 Not Found")

    name, error = fetch_and_save_pokemons(["InvalidPokemon"])

    assert name == "InvalidPokemon"
    assert "404 Not Found" in str(error)


@patch("requests.get")
@patch("service.db.session")
def test_fetch_and_save_pokemons_existing_pokemon(mock_db_session, mock_requests_get, sample_pokemon_response):
    mock_response = MagicMock()
    mock_response.json.return_value = sample_pokemon_response
    mock_response.raise_for_status.return_value = None
    mock_requests_get.return_value = mock_response

    mock_pokemon_query = MagicMock()
    mock_pokemon_query.filter_by.return_value.first.return_value = MagicMock()

    with patch("service.PokemonDTO", new=MockPokemonDTO), \
            patch("service.PokemonDomain", new=MockPokemonDomain), \
            patch("repository.Pokemon.query", new=mock_pokemon_query):
        fetch_and_save_pokemons(["Charmander"])

    mock_db_session.add.assert_not_called()
    mock_db_session.commit.assert_not_called()
