import requests
URL = "https://www.trustpilot.com/review/binance.com?page="
page = requests.get(URL)
print(page.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# # Find elements by id
# results = soup.find(id="__next")
# print(results.prettify())

# # Find element by classname
# reviews = results.find_all("div", class_="styles_reviewContent__0Q2Tg")
# for review in reviews:
#     print(review, end="\n"*2)

# for review in reviews:
#     cus_review = review.find("p", class_="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn")
#     print(cus_review.text.strip(), end="\n"*2)

# Range of page
start = 1
end = 133

for page_number in range(start, end+1):
    url = URL + str(page_number)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")

    reviews = results.find_all("div", class_="styles_reviewContent__0Q2Tg")
    for review in reviews:
        cus_review = review.find("p", class_="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn")
        if cus_review is not None:
            print(cus_review.text.strip(), end="\n"*2)