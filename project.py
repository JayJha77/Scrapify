import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
price = []
Description = []
reviews = []
#for i in range(2,10):

url = "https://www.flipkart.com/search?q=best+mobile+under+20000rs&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_28_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_28_na_na_na&as-pos=2&as-type=RECENT&suggestionId=best+mobile+under+20000rs%7CMobiles&requestId=cbfff848-89eb-47ff-8619-0cf1ccbe75e2&as-searchtext=best+mobile+phone+under+2000&page="+str(1)

r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text,"lxml")
box = soup.find("div",class_="_1YokD2 _3Mn1Gg")

name = box.find_all("div",class_="_4rR01T")


for i in name:
    name = i.text
    Product_name.append(name)
#print(Product_name)

prices = box.find_all("div",class_="_30jeq3 _1_WHN1")


for i in price:
    name = i.text
    price.append(name)
#print(Price)

desc = box.find_all("ul",class_="_1xgFaf")


for i in desc:
    name = i.text
    Description.append(name)
#print(Description)

Reviews = box.find_all("div",class_="_3LWZlK")


for i in Reviews:
    name = i.text
    reviews.append(name)
#print(reviews)

df = pd.DataFrame({"Product_name":Product_name,"prices":prices,"Description":Description,"reviews":reviews})
print(df)

df.to_csv("C:/Users/jayjha/Desktop/git/flipcard_mobile_datset.csv")


   