#!/bin/python3
import sys
import socket
from datetime import datetime
usage ="python3"
if len(sys.argv) == 2 :
	target=socket.gethostbyname(sys.argv[1])
else:
      print("Syntax error")
      print("Invalid number of arguments")

print('-' *50)
print("Scanning target :"+ target)
print("Start time "+ str(datetime.now()))
print('-' *50)

try:
	for port in range(50,85):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result =s.connect_ex((target,port))
if result == 0:
	    print(f"Port {port }found ")
s.close()

except KeyboardInterrupt :
print("\n Exiting program")
sys.exit()
except socket.gaierror :
print("Host name could not be resolved")
sys.exit()
except socket.error:
print("Could not be connectd to the server")
sys.exit()