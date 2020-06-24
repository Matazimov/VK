from rich import print
from cls import cls
import requests
import sys

cls()
token = input("Введите токен: ")
v = 5.21

info = requests.get('https://api.vk.com/method/users.get', params={
        'v': v,
        'name_case': 'Nom',
        'access_token': token,
        'fields': 'photo_max_orig,counters'
    }).json()
if "error" in info:
    print("[red]Неправильный токен[/red]")
    sys.exit()

first_name = info["response"][0]["first_name"]
last_name = info["response"][0]["last_name"]
