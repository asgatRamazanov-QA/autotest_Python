import requests
import pytest


def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/pokemons')
    assert response.status_code==200



def test_fragment_of_response():
    response = requests.get('https://pokemonbattle.me:5000/pokemons',params = {'pokemon_id':'5480'})
    assert response.json()['name'] == 'Уткааа'    