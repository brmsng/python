import requests
from bs4 import BeautifulSoup
import itertools
import pandas as pd
import re


def make_file_name(file_name):
    return file_name.replace('*', '').replace('/', '') + '.jpg'


def download_and_save_image(soup, title_list):
    images = soup.find_all('img', {'src': re.compile(r'.*\.jpg')})

    try:
        for idx, image in enumerate(images):
            res = requests.get('http:' + image['src'])
            with open('images\\' + make_file_name(title_list[idx][0]), 'wb') as f:
                f.write(res.content)
                print(f'{make_file_name(title_list[idx][0])} saved..')
    except Exception as e:
        print(e)


def get_products_by_page_num(page_num=1):
    res = requests.get('http://www.coupang.com/np/rocketdelivery?page=' + str(page_num))
    soup = BeautifulSoup(res.text, 'lxml')

    product_ul_tag = soup.find(id='productList')

    result_list = []
    for li in product_ul_tag.find_all('li', recursive=False):
        try:
            product_name = li.select_one('a > dl > dd > div.name').text
            price = li.select_one('a > dl > dd > div.price-area > div:nth-of-type(1) > div.price > em > strong').text
            rating = li.select_one('a > dl > dd > div.other-info > div.rating-star > span.star > em').text
            rating_total = li.select_one('a > dl > dd > div.other-info > div.rating-star > span.rating-total-count').text
            result_list.append([product_name.strip(), int(price.replace(',', '')), rating, int(rating_total[1:-1])])
        except Exception as e:
            print(e)

        # print(product_name, price, rating, rating_total)
        # result_list.append([product_name, price, rating, rating_total])

    download_and_save_image(product_ul_tag, result_list)
    return result_list


def save_to_csv(list_of_list):
    # 이중리스트를 판다스의 데이터프레임으로 변환
    df = pd.DataFrame(list_of_list, columns=['상품명', '가격', 'rating', 'rating_num'])
    # 데이터프레임을 CSV로 저장
    df.to_csv('coupang.csv', index=False)


def main():
    result = []
    for page_num in itertools.count(1):
        products = get_products_by_page_num(page_num)
        if products == []:
            break
        result.extend(products)
        print(f'page {page_num} scrapped ok..')

    save_to_csv(result)
    print('save to csv.. job completed..')


main()
