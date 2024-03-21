import paramiko

from .models import Server

IP='8.8.8.8'
def ping_ssh(hostname, username, password, ip_address):
    # Connexion SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, username=username, password=password)

    # Commande de ping
    ping_command = f"ping -c 4 {ip_address}"  # Ping 4 fois
    stdout = ssh_client.exec_command(ping_command)

    # Lecture de la sortie du ping
    output = stdout.read().decode('utf-8')

    # Affichage de la sortie et des erreurs
    print("Output:", output)

    # Fermeture de la connexion SSH
    ssh_client.close()



# Utilisation ou l'utilisateur entre les informations
hostname = input("Entrez l'adresse du serveur : ")
username = input("Entrez le nom d'utilisateur : ")
password = input("Entrez le mot de passe : ")
ip_address = IP


ping_ssh(hostname, username, password, ip_address)