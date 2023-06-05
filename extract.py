import requests
URL = "https://www.trustpilot.com/review/binance.com?page="
page = requests.get(URL)
print(page.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Range of page
start = 1
end = 133

# Save review in a text file
output_file = "/Users/mimi/binance_reviews.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for page_number in range(start, end+1):
        url = URL + str(page_number)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="__next")

        reviews = results.find_all("div", class_="styles_reviewContent__0Q2Tg")
        for review in reviews:
            cus_review = review.find("p", class_="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn")
            if cus_review is not None:
                review_text = cus_review.text.strip()
                file.write(review_text + "\n"*2)


