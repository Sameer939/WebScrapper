from bs4 import BeautifulSoup
import requests


def flipkart(product_name):
        url = "https://www.flipkart.com/"
        query = "search?q=" + product_name
        url = url + query

        site = 'Flipkart'

        result = requests.get(url)
        soup = BeautifulSoup(result.content, 'html.parser')

        flipkart_details = []

        if soup.find_all(class_='_31qSD5'):
            for i,mob in enumerate(soup.find_all(class_ = '_31qSD5')):
                try:
                    name = mob.find(class_ = '_3wU53n').text.strip()
                    price = mob.find(class_ = '_1vC4OE _2rQ-NK').text.strip()
                    try:
                        img_det = re.findall("keySpecs(.*?)jpeg", result.text)[i]
                        details = re.findall("\[\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\".*url\":\"(.*)", img_det)[0]
                        url = details[5]
                        url = re.sub("{@width}|{@height}", '250', url) + 'jpeg'
                    except:
                        url = ''
                    try:
                        prod_url = mob.attrs['href']
                        prod_url = "https://www.flipkart.com" + prod_url
                    except:
                        prod_url = ''
                    try:
                        rating = mob.find('div', class_ = 'hGSR34 _2beYZw').text.strip()
                    except:
                        rating = ''
                    try:
                        no_of_ratings = re.findall('(.*)Ratings',mob.find_all('span', class_ = '_38sUEc')[0].text)[0].strip()
                    except:
                        no_of_ratings = ''
                        #no_of_reviews = re.findall('\xa0&\xa0(.*)Reviews',mob.find_all('span', class_ = '_38sUEc')[0].text)[0].strip()
                    flipkart_details.append([name, price, rating, no_of_ratings, site, url, prod_url])
                    #print(site, name, price, url, prod_url)
                except:
                    pass
        else:
            for i,mob in enumerate(soup.find_all('div', class_='_3liAhj _1R0K0g')):
                try:
                    name = mob.find(class_ = '_2cLu-l').text.strip()
                    price = mob.find(class_ = '_1vC4OE').text.strip()
                    try:
                        img_det = re.findall("keySpecs(.*?)jpeg", result.text)[i]
                        details = re.findall("\[\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\".*url\":\"(.*)", img_det)[0]
                        url = details[5]
                        url = re.sub("{@width}|{@height}", '250', url) + 'jpeg'
                    except:
                        url = ''
                    try:
                        prod_url = mob.find(class_ = 'Zhf2z-')
                        prod_url = prod_url.attrs['href']
                        prod_url = "https://www.flipkart.com" + prod_url
                    except:
                        prod_url = ''
                    try:
                        rating = mob.find(class_ = 'hGSR34 _2beYZw').text.strip()
                    except:
                        rating = ''
                    try:
                        no_of_ratings = mob.find(class_ = '_38sUEc').text.strip('()')
                    except:
                        no_of_ratings = ''
                    flipkart_details.append([name, price, rating, no_of_ratings, site, url, prod_url])
#                     print(site, name, price, url, prod_url)
                except:
                    pass
        for i,f in enumerate(flipkart_details):
            print(F"{i}). {f}\n\n")
        return True

def amazon(product_name):
#         url = "https://www.amazon.in/"

        site = 'Amazon'

        url = "https://www.amazon.in/"
        query = "s?k=" + product_name
        url = url + query

        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        r = requests.get(url, headers = header)

        driver = BeautifulSoup(r.content,features="html5lib")


        amazon_details = []
        with open("a.txt", "w", encoding="utf-8") as f:
            f.write(driver.prettify())

        for mob in driver.find_all(class="s-main-slot"):
            try:
                name = mob.find('h2', class_ = 'a-size-base').text.strip()
                price = mob.find('span', class_ = 'a-size-base').text.strip()
                try:
                    prod_url = mob.find(class_ = 'a-link-normal')
                    prod_url = prod_url.attrs['href']
                    if re.search('url=https', prod_url):
                        prod_url = "https://www.amazon.in" + prod_url
                except:
                    prod_url = ''
                try:
                    url = mob.find('img')
                    url = url.attrs['src']
                except:
                    url = ''
                amazon_details.append([name, price, site, url, prod_url])
#                 print(site, name, price, prod_url)
            except:
                try:
                    name = mob.find('h2', class_ = 'a-size-medium').text.strip()
                    price = mob.find('span', class_ = 'a-size-base').text.strip()
                    try:
                        prod_url = mob.find(class_ = 'a-link-normal')
                        prod_url = prod_url.attrs['href']
                        if re.search('url=https', prod_url):
                            prod_url = "https://www.amazon.in" + prod_url
                    except:
                        prod_url = ''
                    try:
                        url = mob.find('img')
                        url = url.attrs['src']
                    except:
                        url = ''
                    amazon_details.append([name, price, site, url, prod_url])
#                     print(site, name, price, prod_url)
                except:
                    pass
        for i,k in enumerate(amazon_details):
            print(F'{i}). {k}\n\n')
        return True

k = input()
# flipkart(k)
print("AMAZON !!!!\n\n")
amazon(k)
