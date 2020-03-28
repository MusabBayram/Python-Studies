import requests
from bs4 import BeautifulSoup

url =  "https://www.youtube.com/watch?v=QY9fx3tBAJs" # Site linkimiz

response =  requests.get(url) # Web sayfamızı çekiyoruz.
print(response)
html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.
#print(soup.prettify())
 # Bu kullanımın anlamı div etiketlerinden class'ı yp-poi-box-2 yi al anlamına geliyor.
for i in soup.find_all("div",{"class":"add-to-widget"}):
    print(i)