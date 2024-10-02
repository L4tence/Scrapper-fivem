import requests

# Fonction pour récupérer les proxies depuis l'API publique
def scrape_mullvad_proxies():
    url = "https://api.mullvad.net/www/relays/openvpn"
    response = requests.get(url)
    if response.status_code == 200:
        proxies = response.json()
        return [proxy["fqdn"] for proxy in proxies]
    else:
        print("Erreur lors de la récupération des proxies depuis l'API Mullvad.")
        return []

# Fonction pour enregistrer les proxies dans un fichier texte
def save_proxies_to_file(proxies, filename="proxy.txt"):
    with open(filename, "w") as file:
        for proxy in proxies:
            file.write(proxy + ":1080\n")
    print(f"{len(proxies)} proxies Mullvad ont été enregistrés dans {filename}!")

# Appel des fonctions pour récupérer et enregistrer les proxies
proxies = scrape_mullvad_proxies()
save_proxies_to_file(proxies)