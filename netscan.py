import subprocess

def run_netscan(target=None):
    """ Hedef IP adresine yönelik ağ taraması yapar. """
    if target is None:
        target = "192.168.1.0/24"  # Default ağ
    try:
        # Hedef ağ üzerinde nmap taraması yapıyoruz
        output = subprocess.check_output(f"nmap -sV {target}", shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Hata: {e.output}\n"
