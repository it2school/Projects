import socket
import sys
import os
os.system("clear")

domain = input("Введите домен(пример www.google.com):")

try:
    ip = socket.gethostbyname( domain )

except socket.gaierror:
        print("Invalid Domain.")
        sys.exit()
print("DNS " + domain + ": IP:" + ip)