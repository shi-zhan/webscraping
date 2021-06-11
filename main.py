import time
from bs4 import BeautifulSoup
import requests
import sys
import pandas as pd

count = 0
page_index = 1
# addresses = []
# names = []
row = []
while True:
    try:

        url = 'https://www.yaoxuanzhi.com/parklist/p' + str(page_index)
        if page_index > 154:
            raise Exception()

        print(url)
        html = requests.get(url).text
        # print(html)
        soup = BeautifulSoup(html, 'lxml')
        parks = soup.find_all('li', class_='park-list-item')
        for park in parks:
            name = park.find('a', class_='title').text
            address = park.find('div', class_='address').text
            park_url = park.find('a').get('href')
            dict = {
                'company_name': name,
                'address': address,
                'park_url': 'https://www.yaoxuanzhi.com' + park_url
            }
            row.append(dict)
            # print(f'Company Name: {name.strip()}\n')
            # print(f'Address: {address.strip()}')
            # print(f'URL: {park_url}')
            # print('')
            count = count + 1

        print(f'one page done: {count}')
        print('')
        time.sleep(5)
        page_index = page_index + 1
    except:
        e = sys.exc_info()[0]
        print(e)
        break
    finally:
        try:
            df = pd.DataFrame(row)
            df.to_csv('parks.csv')
        except:
            e = sys.exc_info()[0]
            print(e)


#
# if __name__ == '__main__':
#     find_parks()
