import os
import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True

titles = []
prices = []
city = []
information = []
DRIVER_PATH = 'D:/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
for i in range(150):
    driver.get(
        'https://www.pakwheels.com/used-cars/search/-/mk_honda/md_civic/?page=' + str(i + 1))  # Only for Honda Civic
    driver.implicitly_wait(5)
    a = driver.find_element_by_xpath("/html/body/div[6]/section[2]/div/div[3]/div[1]/div/div[2]").get_attribute(
        "innerText")
    p = a.splitlines()
    for i in range(len(p)):
        if (p[i].startswith("PKR")):
            print("price: " + p[i])
            print("title: " + p[i + 1])
            print("city: " + p[i + 2])
            print("information: " + p[i + 3])
            titles.append(p[i + 1])
            prices.append(p[i])
            city.append(p[i + 2])
            information.append(p[i + 3])
            print('--------------------')

    print("progress : " +  str((i/150)*100))
driver.close()
df = pd.DataFrame()
df['titles'] = titles
df['price'] = prices
df['city'] = city
df['information'] = information
df.to_csv('./Pakwheels.csv')