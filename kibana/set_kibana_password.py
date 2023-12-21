import requests
import json

url = "https://localhost:9200/_security/user/kibana_system/_password"
headers = {
    "Authorization": "Basic ZWxhc3RpYzpCdVJJVklaRW1LbTZiWVkwMGpQNmFOQkJWMHJjS0Z0Zw==",
    "Content-Type": "application/json"
}

data = {
    "password": "LQYWSVVQxGLueO9NWjr5qQN00J9Z3V2t"
}

response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

if response.status_code == 200:
    print("Mot de passe changé avec succès.")
else:
    print(f"Échec de la requête. Code d'état : {response.status_code}")
    print("Réponse du serveur :")
    print(response.text)
