import pytest
from app import app
from unittest.mock import patch, MagicMock


@patch('app.fetch_and_save_pokemons')
def test_process_pokemons_valid_data(mock_fetch):
    mock_fetch.return_value = (None, None)
    client = app.test_client()
    response = client.post('/process_pokemons',
                           json={'pokemon_names': ['Charmander', 'Bulbasaur']})
    assert response.status_code == 200
    assert response.json == {'message': 'Pokémons processed successfully.'}


def test_process_pokemons_invalid_data():
    client = app.test_client()
    response = client.post('/process_pokemons', json={})
    assert response.status_code == 400
    assert response.json == {
        'error': 'Invalid data. Expected a JSON with a list `pokemon_names`'}


@patch('app.fetch_and_save_pokemons')
def test_process_pokemons_internal_error(mock_fetch):
    mock_fetch.return_value = None
    client = app.test_client()
    response = client.post('/process_pokemons',
                           json={'pokemon_names': ['Charmander']})
    assert response.status_code == 500
    assert response.json == {
        'error': "cannot unpack non-iterable NoneType object"}
