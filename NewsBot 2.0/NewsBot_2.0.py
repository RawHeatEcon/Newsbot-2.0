#Rohit_Kumar
#Newsbot_2.0_Headline_Crawler
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from pynput.keyboard import Key, Controller

#CNN (Static website)
def cnn():
    print("Scanning CNN website...")
    cnn_URL = 'https://www.cnn.com/business'
    cnn_page = requests.get(cnn_URL)
    cnn_raw_code = cnn_page.content
    cnn_source = BeautifulSoup(cnn_raw_code, "html.parser")
    global cnn_headlines
    cnn_headlines = cnn_source.find_all('span', class_='cd__headline-text') 
    print("Scan complete.")
    return cnn_headlines

# Loads website, and then saves html code from news website and searches through the code to match specific 
# html chunk that returns necessary headline text only.

## Note: this is a static website that does not change code through javascript, 
# thus simplifying the scraping process.

#Forbes (Static website)
def forbes():
    print("Scanning Forbes website...")
    forbes_URL = 'https://www.forbes.com/'
    forbes_page = requests.get(forbes_URL)
    forbes_raw_code = forbes_page.content
    forbes_source = BeautifulSoup(forbes_raw_code, "html.parser")
    global forbes_headlines
    forbes_headlines = forbes_source.find_all('a', class_="happening__title")
    print("Scan complete.")
    return forbes_headlines

#Bloomberg (Dynamic website)
def bloomberg():
    print("Scanning Bloomberg website...")
    bloomberg_URL = 'https://www.bloomberg.com/markets/watchlist'
    bloomberg_page = webdriver.Firefox()
    bloomberg_page.get(bloomberg_URL)
    time.sleep(5) # wait 5 seconds for the page to load the js
    bloomberg_raw_code = bloomberg_page.execute_script("return document.documentElement.outerHTML")
    type = Controller()
    type.press(Key.alt)
    type.press(Key.space)
    type.press('c')
    type.release(Key.alt)
    type.release(Key.space)
    type.release('c') 
    #time.sleep(5)
    bloomberg_source = BeautifulSoup(bloomberg_raw_code, "html.parser")
    global bloomberg_headlines
    bloomberg_headlines = bloomberg_source.find_all('a', class_="headline__55bd5397")    
    print("Scan complete.")
    if bloomberg_headlines == ():
        print("ERROR: \n")
        print("Website html has changed, please update code")
    return bloomberg_headlines

# Similar to Static websites, begins by loading the website. 
# Since the website is dynamic, it includes bits of javascript coding that changes the underlying code,
# we pauses our scraping for a few seconds for the page to completely load, and then proceed with the same
# process of static websites.

# Make sure geckodriver executable is in the PATH that way the website can be accessed through the firefox browser

#MarketWatch (Dynamic website)
def marketwatch():
    print("Scanning MarketWatch website...")
    MW_URL = 'https://www.marketwatch.com/'
    MW_page = requests.get(MW_URL)
    MW_raw_code = MW_page.content
    MW_source = BeautifulSoup(MW_raw_code, "html.parser")
    global MW_headlines
    MW_headlines = MW_source.find_all('span', class_='headline')
    print("Scan complete.")
    return MW_headlines

#WallStreetJournal (Static website)
def wall_street_journal():
    print("Scanning Wall Street Journal website...")
    WSJ_URL = 'https://www.wsj.com/news/latest-headlines'
    WSJ_page = webdriver.Firefox()
    WSJ_page.get(WSJ_URL)
    time.sleep(5)
    WSJ_raw_code = WSJ_page.execute_script("return document.documentElement.outerHTML")
    type2 = Controller()
    type2.press(Key.alt)
    type2.press(Key.space)
    type2.press('c')
    type2.release(Key.alt)
    type2.release(Key.space)
    type2.release('c')
    #time.sleep(5)
    WSJ_source = BeautifulSoup(WSJ_raw_code, "html.parser")
    global WSJ_headlines
    WSJ_headlines = WSJ_source.find_all('div', class_='WSJTheme--headline--7VCzo7Ay')
    print("Scan complete.")
    if WSJ_headlines == ():
        print("ERROR: \n")
        print("Website html has changed, please update code")
    return WSJ_headlines

# The code is working as of 11/15/22, future website maintenance may cause problems within the code, and require
# debugging



def scanning():
    cnn()
    forbes()
    bloomberg()
    marketwatch()
    wall_street_journal()


global stock_list1
stock_list1 = []
stock_list1.append("Tesla")
stock_list1.append("Apple")
stock_list1.append("Amazon")
stock_list1.append("Walmart")
stock_list1.append("Google")
stock_list1.append("Facebook")

continue1 = input("Press any key to continue. ")
print("\n")

scanning()

list_of_headlines = []

def display_headlines():
    for cnn_headline in cnn_headlines:
        for stonk in stock_list1:
            if stonk in cnn_headline.text:
                #make a list to add the headlines, so that I can print them or add them to the csv
                list_of_headlines.append(cnn_headline.text)
                print(cnn_headline.text)
    for forbes_headline in forbes_headlines:
        for stonk2 in stock_list1: 
            if stonk2 in forbes_headline.text:
                list_of_headlines.append(forbes_headline.text)
                print(forbes_headline.text)
    for bloomberg_headline in bloomberg_headlines:
        for stonk3 in stock_list1: 
            if stonk3 in bloomberg_headline.text:
                list_of_headlines.append(bloomberg_headline.text)
                print(bloomberg_headline.text)
    for MW_headline in MW_headlines:
        for stonk4 in stock_list1: 
            if stonk4 in MW_headline.text:
                list_of_headlines.append(forbes_headline.text)
                print(forbes_headline.text)
    for WSJ_headline in WSJ_headlines:
        for stonk5 in stock_list1: 
            if stonk5 in WSJ_headline.text:
                list_of_headlines.append(WSJ_headline.text)
                print(WSJ_headline.text)


print("\n")
print("HERE ARE TODAY'S HEADLINES:","\n")
print("___________________________________________________________________________________")
print("\n")
display_headlines()

print("New:")
print(list_of_headlines)



headline_logs = open('headline_logs.csv', 'w')
headline_logs.write("HEADLINES:"+"\n")
#headline_logs.write()
headline_logs.close()



def timestamp():
    now = datetime.now()
    global date_time
    date_time = now.strftime("%H:%M:%S %m/%d/%Y")

timestamp()
headline_logs = open("headline_logs.csv", "a")
headline_logs.write("\n")
headline_logs.write("\n")
headline_logs.write("Accessed: "+date_time)
headline_logs.write("\n")
headline_logs.close()


