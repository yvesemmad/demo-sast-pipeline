# Fichier app.py
import os
def ping_server(ip_address):
   # DANGER : Injection de commande OS possible
   os.system("ping -c 4 " + ip_address)
