import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://example.com"

response = requests.get(url, verify=False)

soup = BeautifulSoup(response.text, "html.parser")

reviews = []

for review in soup.find_all("p"):
    text = review.get_text()
    reviews.append(text)

df = pd.DataFrame(reviews, columns=["Review"])

df.to_csv("reviews.csv", index=False)

print("Reviews collected and saved to reviews.csv")