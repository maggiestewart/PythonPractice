import requests
from bs4 import BeautifulSoup

# define url of webpage to scrape from
url = "https://www.google.com/travel/flights/search?tfs=CBwQAholEgoyMDI1LTEyLTAyKAFqBwgBEgNNU1lyDAgCEggvbS8wNGpwbBolEgoyMDI1LTEyLTA0KAFqDAgCEggvbS8wNGpwbHIHCAESA01TWUABQAFIAXABggELCP___________wGYAQE&tfu=EgQIABABIgMKATA&hl=en&gl=us&client=firefox-b-1-d&curr=USD"

# semd request to get html code from url and save response
response = requests.get(url, headers={"Accept":"text/html"})

# use BeautifulSoup to parse text from the response
parsed_response = BeautifulSoup(response.text, "html.parser")

# find all flight descriptions
descriptions = parsed_response.find_all("div", class_="sSHqwe tPgKwe ogfYpf")

# iterate over the descriptions and print text for each
for d in descriptions:
    print(d.text)
