#!/usr/bin/env python
# 
# TCP Port Scanner Version 1.0.1 (2022)
# 
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool. The author accepts no liability for
# damage caused by this tool.  If these terms are not acceptable to you, then do 
# not use this tool.
# 
# by Pierre CHAUSSARD
# 
# 07-Feb-2022 - 1.0.0 - Creating basic script.
# 10-Feb-2022 - 1.0.1 - Updating README.md & terms of use.


import pyfiglet
import sys
import socket
from datetime import datetime
import json


ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

elif len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1])
    if sys.argv[2]:
        output = sys.argv[3]

else:
    print("Invalid amount of Argument")


print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)


try:
    with open('json/tcp-port.json') as json_data:
            data_dict = json.load(json_data)

    for port in data_dict:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.0000001)

        state = s.connect_ex((target,port['port']))
        if state == 0:
            print(f"{port['port']}/tcp\n |  State : OPEN.\n |  Service : {port['service']}.\n |_ Description : {port['description']}.")
        s.close()

    f = open(f"src/{target}.txt", "a")
    f.write(ascii_banner)
    f.write("-" * 50 + "\n")
    f.write("Scanning Target: " + target + "\n")
    f.write("Scanning started at: " + str(datetime.now()) + "\n")
    f.write("-" * 50 + "\n")

    for port in data_dict:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.0000001)

        state = s.connect_ex((target,port['port']))
        if state == 0:
            f.write(f"{port['port']}/tcp\n |  State : OPEN.\n |  Service : {port['service']}.\n |_ Description : {port['description']}.\n")
        s.close()
    f.close()
    print("\nFile Saved !")


except KeyboardInterrupt:
        print("\n Exiting Program !")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !")
        sys.exit()
except socket.error:
        print("\ Server not responding !")
        sys.exit()
