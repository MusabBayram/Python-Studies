import requests

import sys
url = "http://data.fixer.io/api/latest?access_key=a48bb1c852e9e0ceb4332ada94cc437b"

cevrilen_doviz= input("EUR yu hangi dovize çevirmek istersiniz:")
miktar = float(input("Miktar:"))


response = requests.get(url)

json_verisi = response.json()
try:
    print(json_verisi["rates"][cevrilen_doviz] * miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin")
    sys.stderr.flush()
