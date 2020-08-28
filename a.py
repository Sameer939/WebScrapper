from bs4 import BeautifulSoup
import requests

def amazon(product_name):
#         url = "https://www.amazon.in/"

        site = 'Amazon'

        url = "https://www.amazon.in/"
        query = "s?k=" + product_name
        url = url + query

        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        r = requests.get(url, headers = header)

        driver = BeautifulSoup(r.content,"html5lib")


        amazon_details = []
        # with open("a.txt", "w", encoding="utf-8") as f:
        #     f.write(driver.prettify())
        # print(driver.find_all(class_ = 's-main-slot'))
        # print(driver.prettify())
        if driver.find_all(class_='s-main-slot'):
            for i,mob in enumerate(driver.find_all(class_='s-result-item')):
                if not mob.find(class_='a-price-whole') is None:
                    price = mob.find(class_='a-price-whole').text.strip()
                    name = mob.find(class_="a-size-medium a-color-base a-text-normal").text.strip()
                    prod_url = mob.find(class_='a-link-normal')
                    prod_url = prod_url.attrs['href']
                    prod_url = "https://www.amazon.in" + prod_url
                    print(name,price,"link = ",prod_url)
                    amazon_details.append([name,price,'','',url])


amazon('iPhone 11')
