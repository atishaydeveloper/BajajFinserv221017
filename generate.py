import requests


payload = {
    "name": "Atishay Jain",         
    "regNo": "1164",        
    "email": "atishayjain220751@acropolis.in"  
}


url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"


try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  
    data = response.json()

 
    print("Webhook URL:", data['webhook'])
    print("Access Token:", data['accessToken'])

   
    webhook_url = data['webhook']
    access_token = data['accessToken']

except requests.exceptions.RequestException as e:
    print("Error occurred during webhook generation:", e)
