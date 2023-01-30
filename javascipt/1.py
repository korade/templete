import requests
from bs4 import BeautifulSoup


url = "https://cathyrobertsrealestate.com/"
 #url = "https://lynnrobinson.com/"

html = requests.get(url)

content = html.content
# print(content)
soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify)

output = soup.find('title').text

lst = output.split()

capitalized_url = url

for i in range(len(lst)):
    if lst[i].lower() in capitalized_url:
        capitalized_url = capitalized_url.replace(lst[i].lower(), lst[i].capitalize())

print(capitalized_url)