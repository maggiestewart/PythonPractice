# 1. create a for loop that iterates through each desired page
# 2. combine base url with the current page number
# 3. use requests library to fetch HTML from the url
# 4. use BeautifulSoup library to parse HTML
# 5. extract desired elements from parsed HTML

import requests
from bs4 import BeautifulSoup
from time import sleep

# for loop to iterate over range of page numbers you want to scrape from
# python includes first argument and excludes second argument in range()
for page_number in range(0,48,24):

    # define url
    url = "https://www.allrecipes.com/search?eggplant=eggplant&offset=" + str(page_number) + "&q=eggplant"

    # send request to get html code from url
    response = requests.get(url, headers={"Accept": "text/html"})

    # parse response
    parsed_response = BeautifulSoup(response.text, "html.parser")

    # extract all elements specific to the recipe name from the page
    name_elements = parsed_response.find_all("span", class_="card__title")

    # extract all eleemnts specfic to number of ratings
    ratings_elements = parsed_response.find_all("div", class_="mm-recipes-card-meta__rating-count-number mntl-recipe-card-meta__rating-count-number")

    # print page number
    print("\nPage:", page_number)

    # print recipe name
    print("\nRecipe Name:",list(map(lambda x: x.text.strip(), name_elements)))

    # print number of recipe reviews
    print("\nRecipe Rating:",list(map(lambda x: x.text.strip().split()[0], ratings_elements)))

    # pause program for 1 second between each loop iteration
    sleep(1)