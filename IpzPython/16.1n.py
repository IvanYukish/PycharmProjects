import requests
import bs4

response = requests.get("http://www.codeabbey.com/index/user_ranking")
soup = bs4.BeautifulSoup(response.content)
print(soup)
