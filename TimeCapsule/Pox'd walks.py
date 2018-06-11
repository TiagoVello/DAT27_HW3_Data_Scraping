import pandas as pd
import requests     
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

    
def replays ():
    
    # Inicialization
    browser = webdriver.Chrome('chromedriver.exe')
    browser.implicitly_wait(2) 
    list_replays = []
    # Login
    browser.get(r'https://hsreplay.net/games/mine/#hero=shaman')
    browser.find_element_by_xpath(r'/html/body/div/div/form/p[1]/button'
                                  ).click()
    inputbox = browser.find_element_by_xpath(r'//*[@id="accountName"]')
    inputbox.send_keys('tiago.vello@gmail.com')
    inputbox = browser.find_element_by_xpath(r'//*[@id="password"]')
    inputbox.send_keys('T31g4V2ll4')
    browser.find_element_by_xpath(r'//*[@id="submit"]').click()
    # Search
    browser.find_element_by_xpath(
             r'//*[@id="myreplays-infobox"]/div[3]/div/span[7]/div').click()
    browser.find_element_by_xpath(
             r'//*[@id="myreplays-infobox"]/div[2]/ul/li[1]').click()
    for i in range (1,4):
        # Create a url list for the replays
        for j in range (1,101):
            x=r'//*[@id="my_replays-container"]/div/div[2]/div[2]/div[2]/a[{}]'
            list_replays.append(browser.find_element_by_xpath(x.format(str(i))
            ).get_attribute('href'))
    # Go to the next page
    browser.find_element_by_xpath(
    r'//*[@id="my_replays-container"]/div/div[2]/div[1]/div[1]/nav/ul/li[2]/a'
    ).click
    browser.close()
    return list_replays

# Returns a data frame with the replay info
def info(url):
    row = []
    b = BeautifulSoup(r'https://hsreplay.net/replay/bvFULMmB6ZGn928hwKmGZX')
    
    
    
    
