import socket
import pyfiglet
import os
import sys
import nmap
import time
from pyfiglet import Figlet
from datetime import datetime
from urllib import request as urlrequests

custom_fig = Figlet(font='graffiti')
ascii_banner = pyfiglet.figlet_format("Tracker")
print(ascii_banner)
print("=================================By-547y4m")
 
def tracker():
	soc = socket.socket()
	Sc = nmap.PortScanner()
	print("[$]----Session started---->")
	ip = input("[?]Enter your I.P to Listen on: ") 
 
	try: 
		host = ip
		port = 80
 
		soc.bind((host, 80))
		print("[+] Listening on "+ ip + "....")
		
	except:
		sys.exit("[!]I.P Busy or any other network issue")
		sys.exit(0)
 
	while True:
                
		try:
			soc.listen(5)
			conn, address = soc.accept()
			print("[+] IP Logged " + str(address[0]))
			recon = Sc.scan(address[0],arguments='-O')
			print(str(address[0]) + " OS details : " + recon['scan'][address[0]]['osmatch'][0]['osclass'][0]['osfamily'])
                        
                                        
		except:
			pass
			print("[^]<----Interrupt occured terminating session---->")
			sys.exit(0)
 
tracker()
