import requests
import re


pokemon_info_js_url = 'https://www.pokemon.com/'
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
pokemone_info = requests.get(pokemon_info_js_url, headers=headers)
pokemon_infomation = pokemone_info.text
pokemon_id = re.findall(r'', pokemone_info)

# img_url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/001.png'


# img_resp = requests.get(img_url, headers=headers)
# with open('1.png', 'wb') as f:
#     f.write(img_resp.content)
