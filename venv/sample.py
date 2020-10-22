from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

#using the url to connect to the website
page_url = "https://www.amazon.in/Kurkure-Namkeen-Masala-Munch-95g/dp/B004IF24XE/ref=sr_1_1?dchild=1&keywords=kurkure&qid=1603289038&sr=8-1"
uClient = uReq(page_url)

#using beautiful soup to parse the webpage to read
page_soup = soup(uClient.read(), "html.parser")

#inspecting the website html elments and grbbing the top player names
container1 = page_soup.findAll("div", {"class": "a-row a-spacing-small review-data"})
print(container1)