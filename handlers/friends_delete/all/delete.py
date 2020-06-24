from config import token, v
from .get_id import humans
from rich import print
import requests
import sys

if len(humans) > 0:
    print(f"[purple]У вас {len(humans)} друзей[/purple]")
    confirm = input("Удалить всех друзей? [Да/Нет] ")
    if confirm.lower() == "да":
        print("[cyan]Начинаю удалять...[/cyan]")
    elif confirm.lower() == "нет":
        print("[red]Действие отменено[/red]")
        sys.exit()
    else:
        print("[red]Выберите только из предложенных вариантов[/red]")
        sys.exit()

    i = 0
    while i < len(humans):
        data = requests.post("https://api.vk.com/method/friends.delete", params={
            "v": v,
            "user_id": humans[i],
            "access_token": token
        }).json()
        if "response" in data:
            print(f"[blue]id{humans[i]}[/blue]: Удалил")
        elif "error" in data:
            print(f"[blue]id{humans[i]}[/blue]: Не смог удалить")
        else:
            print("упс... произошла неизвестная ошибка")
            sys.exit()
        i += 1
    print("[green]Все![/green]")
else:
    print("[red]У вас 0 друзей[/red]")
