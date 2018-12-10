import time
from datetime import datetime as dt
path = r"C:\Windows\System32\drivers\etc\hosts"
#path = r"C:\Users\manis\Desktop\imp_docs\hosts"
website_list=["www.facebook.com","www.netflix.com"]
domain="127.0.0.1"
flag=0

while(1):
	if dt(dt.now().year, dt.now().month, dt.now().day,8)<dt.now()<dt(dt.now().year, dt.now().month, dt.now().day,21):
		flag=0
		with open(path,"r+") as fp:
			content = fp.read()
			for em in website_list:
				if em in content:
					pass
				else:
					fp.write("\n"+domain+" "+em)
	else:
		if flag == 0:
			with open(path,"r+") as fp:
				content = fp.readlines()
				fp.seek(0)
				for line in content:
					if not any(witem in line for witem in website_list):
						fp.write(line)
				fp.truncate()
				flag=1
		else:
			pass
	time.sleep(5)