import requests

# === Step 1: Your personal details ===
payload = {
    "name": "Atishay Jain",          # Change to your real name
    "regNo": "1164",         # Change if your actual regNo is different
    "email": "atishayjain220751@gmail.com"  # Use your email
}

# === Step 2: API URL for webhook generation ===
url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

# === Step 3: Make the POST request ===
try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Raise an error for bad HTTP status
    data = response.json()

    # === Step 4: Print and store response details ===
    print("Webhook URL:", data['webhook'])
    print("Access Token:", data['accessToken'])

    # Store for later use
    webhook_url = data['webhook']
    access_token = data['accessToken']

except requests.exceptions.RequestException as e:
    print("Error occurred during webhook generation:", e)
