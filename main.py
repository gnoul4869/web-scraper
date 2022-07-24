import re
import requests
import bs4

FILE_NAME = 'two_stars_titles.txt'
two_stars_titles = []

web_base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
web_named_url = re.search(r'[^http://](.+\.com)', web_base_url).group()

res = requests.get(web_base_url.format(1))

soup = bs4.BeautifulSoup(res.text, 'lxml')

books = soup.select('.product_pod')

print(f"Getting books' titles with 2 stars rating from {web_named_url}...")

print('\n-----------------------------------------------------')
for i in range(1, 51):
    scape_url = web_base_url.format(i)
    res = requests.get(scape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if book.select('.star-rating.Two') == []:
            continue

        book_title = book.select('a')[1]['title']
        print(book_title)
        two_stars_titles.append(book_title)
print('-----------------------------------------------------\n')

print(f'Extracting to {FILE_NAME}...')

with open(f'{FILE_NAME}', 'w+') as f:
    f.write('\n'.join(two_stars_titles))

print('Extraction complete!')
print('Now exiting...')
exit()
