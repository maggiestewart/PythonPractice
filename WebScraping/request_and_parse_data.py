import requests
from bs4 import BeautifulSoup

# define URL
url = "https://www.google.com/travel/flights/search?tfs=CBwQAholEgoyMDI1LTEyLTAyKAFqBwgBEgNNU1lyDAgCEggvbS8wNGpwbBolEgoyMDI1LTEyLTA0KAFqDAgCEggvbS8wNGpwbHIHCAESA01TWUABQAFIAXABggELCP___________wGYAQE&tfu=EgQIABABIgMKATA&hl=en&gl=us&client=firefox-b-1-d&curr=USD"

# send request to get html code from that url
response = requests.get(url, headers={"Accept":"text/html"})

# parse response
parsed_response = BeautifulSoup(response.text, "html.parser")

# format parsed HTML response so it's easier to read and print it out
print(parsed_response.prettify())

