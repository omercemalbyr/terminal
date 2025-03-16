import subprocess
import re
import requests

def get_internal_ip():
    """ Cihazın iç ağ IP adresini alır (Windows). """
    try:
        output = subprocess.check_output("ipconfig", shell=True, stderr=subprocess.STDOUT, text=True)
        # IPv4 adresini buluruz
        match = re.search(r"IPv4\s*Adres[^\w]*(\d+\.\d+\.\d+\.\d+)", output)
        if match:
            return match.group(1)
        else:
            return "IP Adresi bulunamadı"
    except subprocess.CalledProcessError as e:
        return f"Hata: {e.output}"

def get_external_ip():
    """ Dış IP adresini almak için bir HTTP isteği yapar. """
    try:
        response = requests.get("https://api.ipify.org?format=text")
        return response.text.strip()
    except requests.RequestException:
        return "Dış IP alınamadı"
