# import libraries
import requests
import json

print("\nProduct example 1")

base_url = "https://api.upcitemdb.com/prod/trial/lookup"

parameters = {"upc":"025000044908"}

response = requests.get(base_url, params=parameters)

# parse text from API response using JSON
info = json.loads(response.text)

# first item (index = 0)
item = info["items"][0]

# get product title
title = item["title"]

# get brand
brand = item["brand"]

# print title and brand
print("title:", title)
print("brand:", brand)