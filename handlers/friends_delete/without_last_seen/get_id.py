from config import token, v
from rich import print
from cls import cls
import requests
import sys

cls()
print(f"[yellow]Получаю список друзей, у которых включена невидимка...[/yellow]")


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
                if one_id["last_seen"]["time"]:
                    all_id.append(one_id["id"])
            except:
                errors.append(one_id["id"])
    if t["response"]["count"] == len(errors):
        print("[red]У вас включен режим невидимки в приложении VK ME.[/red]\n"
              "Невидимка убирает в ответе от серверов ВК поле [blue]\"был в сети\"[/blue]."
              f"\nПоэтому скрипт считает, что по сути надо удалять всех {len(errors)} друзей.")
        confirm = input("Хотите продолжить? [Да/Нет] ")
        if confirm.lower() == "да":
            pass
        elif confirm.lower() == "нет":
            print("[red]Действие отменено[/red]")
            sys.exit()
    return errors


humans = get_id()
