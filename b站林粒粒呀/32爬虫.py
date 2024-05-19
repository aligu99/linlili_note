# import requests
# response = requests.get('http://books.toscrape.com/')
# if response.ok:
#     print(response.text)
# else:
#     print('请求失败')


# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
# }
# response = requests.get('http://movie.douban.com/top250', headers=headers)
# print(response.text)


# from bs4 import BeautifulSoup
# import requests
# content = requests.get('http://books.toscrape.com/').text
# soup = BeautifulSoup(content, 'html.parser')
# all_titles = soup.findAll('h3')
# for title in all_titles:
#     all_links = title.findAll('a')
#     for link in all_links:
#         print(link.string)


import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
for start_num in range(0, 250, 25):
    response = requests.get(f'http://movie.douban.com/top250?start={start_num}', headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    all_titles = soup.findAll('span', attrs={'class': 'title'})
    for title in all_titles:
        title_string = title.string
        if '/' not in title_string:
            print(title_string)
