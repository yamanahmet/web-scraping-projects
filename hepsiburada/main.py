from bs4 import BeautifulSoup
import requests
import time

start_time = time.time()
base_url = "https://www.hepsiburada.com/"

category_list = ["bilgisayarlar-c-2147483646", "yazicilar-c-3013118", "telefonlar-c-2147483642", "ses-goruntu-sistemleri-c-17201", "beyaz-esya-ankastreler-c-235604", "isitma-sogutma-urunleri-c-161876", "elektrikli-ev-aletleri-c-17071", "foto-kameralari-c-2147483606", "oyunlar-oyun-konsollari-c-2147483602"]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

product = ["product_name", "product_price"]


def data(cat_url):
    for page_number in range(1, 10):
        url = cat_url + "?sayfa=" + str(page_number)
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "lxml")

        product_names = soup.find_all("h3", attrs={"data-test-id":"product-card-name"})
        prices = soup.find_all("div", attrs={"data-test-id":"price-current-price"})

        for k in range(len(product_names)):
            product[0] = product_names[k].getText()
            product[1] = prices[k].getText()
            print(product)


for i in range(9):
    print("\n************Kategori ismi: " + category_list[i] + "************************")
    category_url = base_url + category_list[i]
    data(category_url)


print("--- %s seconds ---" % (time.time() - start_time))