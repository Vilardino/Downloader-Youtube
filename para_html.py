from bs4 import BeautifulSoup
import requests


def gen_html(html):
    try:
        soup = BeautifulSoup(requests.get(html).text, 'html.parser')
        links = open('links.txt', 'w')

        for a in soup.select('a[href*="/watch?"]')[2:]:
            leitura = 'https://www.youtube.com{}'.format(a['href'])
            if('&index=' in leitura):
                link = 'https://www.youtube.com{}'.format(a['href'])
                links.write(link + '\n')
        print('Ja localizamos todos os links')
        links.close()
    except:
        print("Tive problemas com a lista")