import subprocess

def run_ipconfig():
    try:
        # Windows ipconfig komutunu çalıştırıyoruz
        output = subprocess.check_output("ipconfig", shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Hata: {e.output}\n"
