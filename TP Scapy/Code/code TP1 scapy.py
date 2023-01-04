#importation des bibliothèques
from scapy.all import *
import random
import time

#La fonction syn_scan_ip effectue un balayage SYN sur l'adresse IP et le port donnés.
#Si aucune réponse n'est reçue, la fonction renvoie "Pas de réponse".
#Si une réponse TCP est reçue avec des drapeaux "SYN/ACK", cela signifie que le port est ouvert et la fonction renvoie "Ouvert".
#Si une réponse TCP est reçue avec des drapeaux "RST", cela signifie que le port est fermé et la fonction renvoie "fermé".
def syn_scan(ip, port, timeout):
  response = sr1(IP(dst=ip)/TCP(dport=port, flags='S'), timeout=timeout, verbose=0)
  if response is None:
    # Pas de réponse
    return "Pas de réponse"
  elif response.haslayer(TCP):
    if response.getlayer(TCP).flags == 0x12:
      # Réponse SYN/ACK, port ouvert
      # la ligne de code envoie une demande de réinitialisation de connexion (RST) au port cible en utilisant la fonction sr.
      send_rst = sr(IP(dst=ip)/TCP(dport=port, flags='R'), timeout=timeout, verbose=0)
      return "Ouvert"
    elif response.getlayer(TCP).flags == 0x14:
      # Réponse RST, port fermé
      return "fermé"


# Creation de la seconde fonction
# Pour activer le mode "stealth", notre programme envoie un paquet TCP avec les flags RST (0x04) 
# au port cible lorsqu'il reçoit un paquet SYN/ACK. Cela a pour effet de mettre fin 
# à la demande de connexion et d'éviter de laisser une trace dans les journaux d'activités de la cible.
def stealth_syn_scan(ip_scan, debut_port, fin_port):
    for port in range(debut_port, fin_port+1):
        resp = sr1(IP(dst=ip_scan)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
        if resp is None:
            continue
        if resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:
                print("Port {}: Open".format(port))
                send_rst = sr(IP(dst=ip_scan)/TCP(dport=port, flags="R"), timeout=1, verbose=0)



# Ce code demande à l'utilisateur de choisir entre l'exécution du programme 1 ou 2. 
# Si l'utilisateur choisit "1", le programme effectue un balayage SYN sur la plage de ports de 50 à 1024 de l'adresse IP "192.168.1.1" et affiche le statut de chaque port. 
# Si l'utilisateur choisit "2", le programme exécute la fonction stealth_syn_scan sur l'adresse IP "192.168.1.1" et la plage de ports de 50 à 1024. 
# Si l'utilisateur ne fait aucun de ces choix, le programme affiche un message d'erreur.
choix=input("Veux choisir le programme a lancer 1 ou 2 \n")
if choix == "1":
   #Pour exécuter un SYN scan sur la plage de ports 50 à 1024
   #Modification de l'ip
  ip = "192.168.1.1"
  timeout = 1 # Délai en secondes
  for port in range(50, 1024):
    status = syn_scan(ip, port, timeout)
    print(f"Port {port}: {status}")
elif choix == "2":
  stealth_syn_scan(ip_scan, debut_port, fin_port)
  ip_scan = "192.168.1.1"
  debut_port = 50
  fin_port = 1024
else:
  print("Vous avez fais un mauvais choix")