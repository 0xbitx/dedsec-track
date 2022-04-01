import os

def cloudflare():
	print()
	os.system("rm .cld.log")
	os.system("./cloudflared tunnel -url 127.0.0.1:8080 --logfile .cld.log")

cloudflare()
