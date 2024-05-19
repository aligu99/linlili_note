from bs4 import BeautifulSoup
import requests

response = requests.get('http://books.toscrape.com/')
if response.ok:
    print(response.text)
else:
    print('请求失败')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
response = requests.get('http://movie.douban.com/top250', headers=headers)
print(response.text)


content = requests.get('http://books.toscrape.com/').text
soup = BeautifulSoup(content, 'html.parser')
all_titles = soup.findAll('h3')
for title in all_titles:
    all_links = title.findAll('a')
    for link in all_links:
        print(link.string)
