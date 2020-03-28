import requests

import sys
url = "https://kur.doviz.com/serbest-piyasa/euro"
#cevrilen_doviz= input("EUR yu hangi dovize çevirmek istersiniz:")
#miktar = float(input("Miktar:"))


response = requests.get(url)
print("adsfasf")
json_verisi = response.json()
try:
    print(json_verisi["value"] * miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin")
    sys.stderr.flush()
