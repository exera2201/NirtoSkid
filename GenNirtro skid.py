import colorsys
import random 
import time
import socket  

from pystyle import *



skidProjet = """                      )                 
       )    (      ( /(           )     
    ( /((   )\ )   )\())(  (   ( /(     
 (  )\())\ (()/(  ((_)\ )\ )(  )\())(   
 )\((_)((_) ((_))  _((_|(_|()\(_))/ )\  
((_) |(_|_) _| |  | \| |(_)((_) |_ ((_) 
(_-< / /| / _` |  | .` || | '_|  _/ _ \ 
/__/_\_\|_\__,_|  |_|\_||_|_|  \__\___/ 
                                        
"""


print(Colorate.Vertical(Colors.white_to_blue, skidProjet))

time.sleep(1)
print(Col.red + "Attention les skid!")

time.sleep(20)

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

while True:
	nitro = ''

	for i in range(10):
		nitro = f"{nitro}{random.choice(chars)}"

	print(f"https://discord.gift/{nitro}")

	with open("pour les skid.txt", "a+") as file:
		file.write(f"https://discord.gift/{nitro}\n")
		file.close()



