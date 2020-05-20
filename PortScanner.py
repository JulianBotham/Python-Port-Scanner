"""
PORT SCANNER 20-1000
Created by: JBWJB
Thanks to TheCyberMentor
"""

import sys
import socket
from datetime import datetime

#Define Target
if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
else:
        print("Invalid amount of arguments")
        print("Syntax: python3 PortScanner.py <ip>")

print("-" * 50)
print("\nScanning target..." + target)
print("\nTime started" + str(datetime.now()))

try:
    for port in range(20,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
            s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Host name could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()


