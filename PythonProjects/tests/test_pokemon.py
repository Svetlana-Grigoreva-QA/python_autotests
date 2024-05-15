import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'ТОКЕН ТРЕНЕРА'
HEADER ={"Content-type" : "application/json",
          "trainer_token" : TOKEN
        }
TRAINER_ID = "ID ТРЕНЕРА"

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json() ["data"][0]["trainer_name"] == "ИМЯ ТВОЕГО ТРЕНЕРА"

