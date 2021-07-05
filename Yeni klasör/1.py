 
import requests
from bs4 import BeautifulSoup 
from send_mail import sendMail

url1='url'

headers={'User-Agent':''}
page = requests.get(url1, headers=headers)
htmlPage=BeautifulSoup(page.content,'html.parser')
productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

price = htmlPage.find("span", class_="prc-slg").getText()

image=htmlPage.find("img", class_="ph-gl-img")

convertedPrice= float(price.replace(",",".").replace("TL",""))
print(convertedPrice)

if(convertedPrice <= 500):
    print("ürün fiyatı düştü")
    htmlEmailContent ="""\
         <html>
         <head></head>
         <body>
         <h3>{0}</h3>
         <br/>
         {1}
         <br/>
         <p>ürün linki:{2}<p/>
         </body>
         </html>

         """.format(productTitle,image,url1)
    sendMail("mail","Ürünün fiyatı düştü",htmlEmailContent)

print(convertedPrice)

