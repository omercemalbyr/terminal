import subprocess

def run_netdiscover(target=None):
    """ Hedef IP adresine yönelik netdiscover çalıştırır. """
    if target is None:
        target = "192.168.1.0/24"  # Default ağ
    try:
        # Hedef ağda cihazları keşfetmek için netdiscover komutunu çalıştırıyoruz
        output = subprocess.check_output(f"netdiscover -r {target}", shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Hata: {e.output}\n"
