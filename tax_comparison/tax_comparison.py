import os
from unicodedata import name
# from click import option
# from requests import options
from selenium import webdriver
from sqlalchemy import false
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from tqdm import tqdm
from pathlib import Path
import time

import uuid
import urllib.request


import pandas as pd


individual_currency = {}



open_all_button = False

class Scraper:
    def __init__(self) -> None:

        self.url = f'https://www.x-rates.com/table/?from=GBP&amount=1'
        # s = ChromeDriverManager().install()
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1024,768')
        # if headless:
        #     options.add_argument('--headless')
        #     self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #     # self.driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options)
            
        # else:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.url)


if __name__ == '__main__':

    '''
    Things to do:
    1.
    Find a way to scrape the currency converter from the 'x-rates' site

    2.
    Create a dictionary that attaches the original country as the key and the exchange rate as the value

    3.
    a) Add the tax bracket for each country
    b) Use the dictionary to convert each bracket into pounds
    c) Create a program to calculate the amount you would be taxed per year
    d)  
    
    
    '''
    bot = Scraper()
    time.sleep(3)
    data = []
    cont = bot.driver.find_element_by_xpath('//table[@class="tablesorter ratesTable"]')
    elements = cont.find_elements_by_tag_name('tr')
    num_cont = len(elements)
    for i in range(num_cont):
        table = bot.driver.find_element_by_xpath('//table[@class="tablesorter ratesTable"]')
        elements = cont.find_elements_by_tag_name('tr')[i]

        new_data = elements.text
        print(new_data)
        data.append(new_data)
    data.pop(0)
    new_lst = list
    # for i in data:
    #     new_str = str.split(i)
    #     data.append(new_str)
    # print(data)
    # for val in new_str:
    #     if len(val) == 5:
    #         currency = val.join((val[0],val[1],val[2]))
    #         new_lst.append(new_str)
    #     else:
    #         currency = val.join((val[0],val[1]))
    #         new_lst.append(new_str)        
    # print(new_lst)   
        # x = new_str[0]
        # y = float(new_str[2])
        # individual_currency
    # print(table)
    # new_data = bot.driver.find_element(by=By.TAG_NAME, value='tr')
    # data.append(new_data)
    # print(data)
    bot.driver.quit()
    # wage = input("Your annual wage:  ")


    # if wage <= 32687.03:
    #     first_bracket = 0.15 * wage
    # else:
    #     if wage <= 65373:
    #         second_bracket = 
