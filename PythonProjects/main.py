import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'ТОКЕН ТРЕНЕРА'
HEADER = {"Content-type" : "application/json",
          "trainer_token" : TOKEN
        }
body_creation = {
    "email" : "МЭИЛ",
    "password" : "ПАРОЛЬ",
    "name" : "Worqav",
    "photo" : "https://dolnikov.ru/pokemons/albums/003.png"
}
body_name = {
    "pokemon_id": "ID ПОКЕМОНА",
    "name": "New",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_pokeball = {
    "pokemon_id": "ID ПОКЕМОНА"
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response)

response_name = requests.put(url=f'{URL}/pokemons', headers= HEADER, json = body_name)
print(response_name.text)

response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers= HEADER, json=body_pokeball)
print(response_pokeball.text)