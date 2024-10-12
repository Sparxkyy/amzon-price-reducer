import requests
from bs4 import BeautifulSoup
import smtplib
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()
date=dt.datetime.now()






URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response=requests.get(url=URL)
response.raise_for_status()
webpage_text=response.text
soup=BeautifulSoup(webpage_text, "html.parser")

price=soup.find(name="span",class_="a-price-whole")
price_tag=float(price.get_text())
print(price_tag)
max=90
if price_tag<max:

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        sender = connection.login(user=os.environ["my_email"], password=["password"])
        connection.sendmail(from_addr=os.environ["my_email"], to_addrs="pariyultiwari99@gmail.com",
                            msg=f"price is dropped to {price_tag} buy it!!!")

