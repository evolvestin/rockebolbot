import requests

url = "https://api.telegram.org/bot462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
