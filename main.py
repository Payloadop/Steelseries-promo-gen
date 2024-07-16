import requests
import re
import tls_client
import warnings
import os
from mailtm import Email
from urllib3.exceptions import InsecureRequestWarning
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By



#Join https://discord.gg/uzCQ2HzaKs



warnings.simplefilter('ignore', InsecureRequestWarning)

client = tls_client.Session(
    client_identifier='chrome_120',
    random_tls_extension_order=True
)

def listener(message):
    global verification_url
    pattern = r'https://accounts\.steelseries\.com/verify\?token=\S+'
    urls = re.findall(pattern, message['text'])
    if urls:
        verification_url = urls[0]

def create_account(email_service):
    email_service.register()
    email = str(email_service.address)

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) steelseries-gg-client/3.0.0 Chrome/110.0.5481.179 Electron/23.1.3 Safari/537.36"
    }

    payload = {
        "email": email,
        "password1": "PapaPayl0d",
        "password2": "PapaPayl0d",
        "acceptedPrivacyPolicy": True
    }
    print(f"Generating Using : {email}")

    try:
        r = requests.post("https://127.0.0.1:6327/user", verify=False, headers=headers, json=payload)
        r.raise_for_status()
        data = r.json()  
        if r.status_code == 200:
            username = data["user"]["username"]
            email = data["user"]["email"]
            print(f"Sent Email Verify Link : Username : {username} : Email : {email}")  
            return email
        else:
            print(f"Failed {r.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        return None
    except ValueError:
        print("Error parsing JSON response")
        return None

def verify_account(email_service, email):
    global verification_url
    verification_url = None

    email_service.start(listener)
    print("Waiting for verification email...")

    timeout = 120  
    start_time = time.time()

    while verification_url is None and time.time() - start_time < timeout:
        time.sleep(5)

    if verification_url:
        print(f"Verification URL: {verification_url}")

        input("")

        print("Verification complete. Fetching promo code...")

        payload = {
            "name": "giveaway_discord_jul01"
        }
        try:
            reques = requests.post("https://127.0.0.1:6327/promos/code", verify=False, json=payload)
            reques.raise_for_status()  
            req = reques.json()  

            promo_code_url = req.get("promocode", "")
            print(f"Promo: {promo_code_url}")
            with open("Promos.txt", 'a') as f:  
                f.write(f"{promo_code_url}\n")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching promo code: {e}")
    else:
        print("No verification URL found within the timeout period.")

if __name__ == '__main__':
    email_service = Email()  
    genned = 0
    # Part Taken From Sysys Old Gen :)
    while True:
        if genned == 4:
            time.sleep(40)
            genned = 0
        os.system('taskkill /f /IM SteelSeriesGGClient.exe')
        os.system('start cmd /c "C:\\Program Files\\SteelSeries\\GG\\SteelSeriesGGClient.exe"')
        time.sleep(1)
        email = create_account(email_service)
        if email:
            verify_account(email_service, email)
        else:
            print("Failed to create account, retrying...")
        time.sleep(1)
        genned += 1
