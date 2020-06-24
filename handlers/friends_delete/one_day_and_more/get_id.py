from config import token, v
from rich import print
from cls import cls
import requests
import time
import sys

cls()
print(f"[yellow]Получаю список друзей...[/yellow]")
one_day = 86400
unix = time.time()


def get_id():
    all_id = []
    errors = []
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
            "fields": "last_seen",
            "access_token": token
        }).json()
        if "response" not in data:
            print("[red]Произошла ошибка[/red]")
            sys.exit()
        offset += 1000
        for one_id in data["response"]["items"]:
            try:
                if one_id["last_seen"]["time"] < (unix - one_day):
                    all_id.append(one_id["id"])
            except:
                errors.append(one_id["id"])
    if t["response"]["count"] == len(errors):
        print("[red]У вас включен режим невидимки в приложении VK ME.[/red]\n"
              "Невидимка убирает в ответе от серверов ВК поле [blue]\"был в сети\"[/blue]."
              "\nПоэтому скрипт не может понять, кто не заходил больше дня."
              "\nОтключите невидимку, чтобы вы могли пользоваться этой функцией.")
        sys.exit()
    return all_id


humans = get_id()
