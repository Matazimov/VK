from config import token, first_name, last_name, v
from rich import print
from cls import cls
import requests
import sys

cls()
group_id = input(f"({first_name} {last_name}) Введите id группы/страницы: ")
print("[yellow]Получаю список пользователей...[/yellow]")


def get_id():
    id_domain = "owner_id" if "-" in group_id else "domain"
    all_id = []
    offset = 0

    while offset < 1000:
        data = requests.get("https://api.vk.com/method/wall.get", params={
            "v": v,
            "count": 100,
            "offset": offset,
            "filter": "others",
            "access_token": token,
            f"{id_domain}": group_id
        }).json()
        if "response" not in data:
            print("[red]Произошла ошибка[/red]")
            sys.exit()
        offset += 100
        for one_id in data["response"]["items"]:
            all_id.append(one_id["from_id"])
    return list(set(all_id))


humans = get_id()
