from config import token
from rich import print
from cls import cls
import requests
import sys

cls()
print("[yellow]Получаю список пользователей...[/yellow]")


def get_id():
    data = requests.get("https://api.vk.com/method/friends.getSuggestions", params={
        "v": 5.103,
        "count": 500,
        "filter": "mutual",
        "access_token": token,
        "fields": "friend_status"
    }).json()
    if "response" not in data:
        print("[red]Произошла ошибка[/red]")
        sys.exit()
    data_filter = list(filter(lambda x: x["friend_status"] == 0, data["response"]["items"]))
    return data_filter


humans = get_id()
