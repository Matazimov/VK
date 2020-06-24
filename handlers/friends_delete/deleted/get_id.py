from config import token, v
from rich import print
from cls import cls
import requests
import sys

cls()
print(f"[yellow]Получаю список друзей...[/yellow]")


def get_id():
    all_id = []
    offset = 0

    t = requests.get("https://api.vk.com/method/friends.get", params={
        "v": v,
        "count": 1,
        "access_token": token
    }).json()

    if "response" not in t:
        print("[red]Произошла ошибка[/red]")
        sys.exit()

    while offset < t["response"]["count"]:
        data = requests.get("https://api.vk.com/method/friends.get", params={
            "v": v,
            "count": 1000,
            "offset": offset,
            "fields": "sex",
            "access_token": token
        }).json()
        if "response" not in data:
            print("[red]Произошла ошибка[/red]")
            sys.exit()
        offset += 1000
        for one_id in data["response"]["items"]:
            try:
                if one_id["deactivated"]:
                    all_id.append(one_id["id"])
            except:
                pass
    return all_id


humans = get_id()
