from .get_id import humans
from config import token, v
from rich import print
import requests
import sys

if len(humans) > 0:
    print(f"Вконтакте вернул {len(humans)} рекомендованных друзей")
    print("[cyan]Начинаю добавлять...[/cyan]")
    i = 0
    while i < len(humans):
        data = requests.post("https://api.vk.com/method/friends.add", params={
            "v": v,
            "access_token": token,
            "user_id": humans[i]["id"]
        }).json()
        if "response" in data:
            print(f"[blue]id{humans[i]['id']}[/blue]: Добавил")
        elif "error" in data:
            if data['error']["error_code"] == 14:
                captcha_sid = data['error']["captcha_sid"]
                print(f"Введите код с капчи:\nhttps://api.vk.com/captcha.php?"
                      f"sid={captcha_sid}")
                code = input()
                data_captcha = requests.post('https://api.vk.com/method/friends.add', params={
                    'user_id': humans[i]["id"],
                    'v': v,
                    'access_token': token,
                    'captcha_sid': captcha_sid,
                    'captcha_key': code
                }).json()
                if "response" in data_captcha:
                    print("[green]Верно[/green]")
                    print(f"[blue]id{humans[i]['id']}[/blue]: Добавил")
                elif "error" in data_captcha:
                    if data_captcha["error"]["error_code"] == 14:
                        print("[red]Неверно[/red]")
                else:
                    print("упс... произошла неизвестная ошибка")
                    sys.exit()
            elif data["error"]["error_code"] == 1:
                print("[green]Лимит на добавления в друзья[/green]")
                sys.exit()
        else:
            print("упс... произошла неизвестная ошибка")
            sys.exit()
        i += 1
    print("[green]Все![/green]")
else:
    print("[red]Вконтакте пока что не подготовил рекомендованных друзей(([/red]")
