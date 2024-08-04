from bs4 import BeautifulSoup
import requests

# URL Hacker News
url = "https://news.ycombinator.com/"

# Отримати контент
content = requests.get(url).content

# Створити екземпляр soup
soup = BeautifulSoup(content, "html.parser")

# Знайти всі заголовки статей
headlines = soup.find_all("span", class_="titleline")

# Надрукувати всі заголовки
for index, headline in enumerate(headlines, start=1):
    print(f"{index}. {headline.get_text()}")
