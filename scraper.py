import requests

url = "https://www.ceneo.pl/91714422"
response = requests.get(url)

print(response.status_code)

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["date-enty-id"]
author = opinion.select_one("span.user-post__author-name")
print(author)
recommendation = opinion.select_one("span.user=post__author-name").get_text().strip()
stars_amount = opinion.select_one("span.user-post__score-count").get_text().strip()
content = opinion.select_one("div.user-post__text").get_text().strip()
opinion_date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
transaction_date = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]


#Komentarz kontrolny