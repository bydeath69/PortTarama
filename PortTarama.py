#python 3.7.1
import os
import sys

os.system("clear")
banner="""

____   ___  ____ _____
|  _ \ / _ \|  _ \_   _|
| |_) | | | | |_) || |    Coder By Death
|  __/| |_| |  _ < | |    Port TaramaV1.0
|_|    \___/|_| \_\|_|

Port Tarama Araci

"""

print (banner)
Hedef_ip=raw_input("Hedef ip: ")
os.system("figlet Tarama Basliyor")
os.system("clear && nmap -sV "+Hedef_ip)
print ("Nmap Taramasi Tamamlanmistir")
input ("")
