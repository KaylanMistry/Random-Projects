import os
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
    
    def find_currency_table(self):
        cont = bot.driver.find_element_by_xpath('//table[@class="tablesorter ratesTable"]')
        elements = cont.find_elements_by_tag_name('tr')
        num_cont = len(elements)
        for i in range(num_cont):
            table = bot.driver.find_element_by_xpath('//table[@class="tablesorter ratesTable"]')
            elements = cont.find_elements_by_tag_name('tr')[i]

            new_data = elements.text
            data.append(new_data)
        data.pop(0)
        return data

    def get_currency_dict(self):
        for currencies in data:
        # The currencies are the individual currencies within the 'data' list
            x = currencies.split() # This splits all the currencies and assigns it to the variable x
            new_lst.append(x) # new_lst now contains each individual currency split into strings for each eg. ['Icelandic', 'Krona', '162.824469', '0.006142']    
        for lsts in new_lst:
            if len(lsts) == 5:
                currency_string = [''.join(lsts[0]+' '+lsts[1]+' '+lsts[2]), float(lsts[3]), float(lsts[4])]
                finished_lst.append(currency_string)
                pass
            if len(lsts) == 4:
                currency_string1 = [''.join(lsts[0]+' '+lsts[1]), float(lsts[2]), float(lsts[3])]
                finished_lst.append(currency_string1)
                pass
            if len(lsts) == 3:
                currency_string2 = [lsts[0], lsts[1], float(lsts[2])]
                finished_lst.append(lsts)
                pass
            
            else:
                pass
        for fin_currency in finished_lst:
            dict_currency = [fin_currency[0], fin_currency[-1]]
            individual_currency.update([dict_currency])
        return individual_currency



if __name__ == '__main__':

    '''
    Things to do:
    1.
    Find a way to scrape the currency converter from the 'x-rates' site
    DONE
    2.
    Create a dictionary that attaches the original country as the key and the exchange rate as the value
    DONE
    3.
    a) Add the tax bracket for each country
    b) Use the dictionary to convert each bracket into pounds
    c) Create a program to calculate the amount you would be taxed per year
    d) Create a function to compare this to another country

    4.
    Find a way to save the dictionary when you have scraped it initially.  (Not having to scrape the site again until an hour or so has passed)

    5. 
    Make sure it runs with no bugs and is user friendly
    
    
    '''
    bot = Scraper()
    time.sleep(3)
    data = []
    bot.find_currency_table()
    new_lst = []
    finished_lst = []
    bot.get_currency_dict()
    print(individual_currency)

    bot.driver.quit()
    # wage = input("Your annual wage:  ")


    # if wage <= 32687.03:
    #     first_bracket = 0.15 * wage
    # else:
    #     if wage <= 65373:
    #         second_bracket = 
