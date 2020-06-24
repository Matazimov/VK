from config import token, v
from .get_id import humans
from rich import print
import requests
import sys

if len(humans) > 0:
    print(f"[purple]Вконтакте вернул {len(humans)} заблокированных/"
          f"удаленных/замороженных друзей[/purple]\n[cyan]Начинаю удалять...[/cyan]")

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
    print("[green]У вас нет заблокированных друзей[/green]")
