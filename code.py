import re
import requests

def extract_cfx_re_values(text):
    cfx_re_values = re.findall(r'(?<=\x06)(.*?)(?=\x12)', text)
    return cfx_re_values

def clean_cfx_re_value(value):
    cleaned_value = ''.join(char for char in value if 32 <= ord(char) <= 126)
    if cleaned_value.strip() and cleaned_value.isalnum():
        return cleaned_value
    else:
        return ""
api_url = "https://servers-frontend.fivem.net/api/servers/stream/1710750750/"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; S23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Mobile Safari/537.36"
}

try:
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        cfx_re_values = extract_cfx_re_values(response.text)

        if cfx_re_values:
            with open("serveur.txt", "w", encoding="utf-8") as file:
                for cfx_re_value in cfx_re_values:
                    cleaned_value = clean_cfx_re_value(cfx_re_value)
                    if cleaned_value and "locale" not in cleaned_value:
                        file.write(cleaned_value + "\n")

            print("Valeurs de cfx.re enregistrÃ©es dans le fichier serveur.txt")
        else:
            print("Aucune valeur de cfx.re n'a Ã©tÃ© trouvÃ©e dans la rÃ©ponse de l'API.")
    else:
        print("La requÃªte a Ã©chouÃ© avec le code :", response.status_code)

except requests.RequestException as e:
    print("Erreur lors de la requÃªte :", e)