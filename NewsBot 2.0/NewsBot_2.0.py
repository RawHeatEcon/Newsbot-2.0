#Rohit_Kumar
#Newsbot_2.0_Headline_Crawler
import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from pynput.keyboard import Key, Controller
from csv import writer



def scrape_logger():
    #CNN (Static website)
    def cnn():
        #print("Scanning CNN website...")
        cnn_URL = 'https://www.cnn.com/business'
        cnn_page = requests.get(cnn_URL)
        cnn_raw_code = cnn_page.content
        cnn_source = BeautifulSoup(cnn_raw_code, "html.parser")
        global cnn_headlines
        cnn_headlines = cnn_source.find_all('span', class_='cd__headline-text') 
        #print("Scan complete.")
        return cnn_headlines
    #Forbes (Static website)
    def forbes():
        #print("Scanning Forbes website...")
        forbes_URL = 'https://www.forbes.com/'
        forbes_page = requests.get(forbes_URL)
        forbes_raw_code = forbes_page.content
        forbes_source = BeautifulSoup(forbes_raw_code, "html.parser")
        global forbes_headlines
        forbes_headlines = forbes_source.find_all('a', class_="happening__title")
        #print("Scan complete.")
        return forbes_headlines
    #Bloomberg (Dynamic website)
    def bloomberg():
        #print("Scanning Bloomberg website...")
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
        #print("Scan complete.")
        if bloomberg_headlines == ():
            print("ERROR: \n")
            print("Website html has changed, please update code")
        return bloomberg_headlines
    #MarketWatch (Dynamic website)
    def marketwatch():
        #print("Scanning MarketWatch website...")
        MW_URL = 'https://www.marketwatch.com/'
        MW_page = requests.get(MW_URL)
        MW_raw_code = MW_page.content
        MW_source = BeautifulSoup(MW_raw_code, "html.parser")
        global MW_headlines
        MW_headlines = MW_source.find_all('span', class_='headline')
        #print("Scan complete.")
        return MW_headlines
    #WallStreetJournal (Static website)
    def wall_street_journal():
        #print("Scanning Wall Street Journal website...")
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
        #print("Scan complete.")
        if WSJ_headlines == ():
            print("ERROR: \n")
            print("Website html has changed, please update code")
        return WSJ_headlines

    def tsla():
        #print("Scanning tsla stock price...")
        tsla_URL = 'https://www.cnbc.com/quotes/TSLA'
        tsla_page = requests.get(tsla_URL)
        tsla_raw_code = tsla_page.content
        tsla_source = BeautifulSoup(tsla_raw_code, "html.parser")
        global tsla_price
        tsla_price = tsla_source.find('span', class_='QuoteStrip-lastPrice') 
        #print("Scan complete.")
        #print(tsla_price.text)
        return tsla_price

    def scanning():
        cnn()
        forbes()
        bloomberg()
        marketwatch()
        wall_street_journal()
        tsla()

    global stock_list1
    stock_list1 = []
    stock_list1.append("Tesla")
    stock_list1.append("Elon")
    stock_list1.append("Musk")
    stock_list1.append("Space")
    stock_list1.append("SpaceX")
    stock_list1.append("Electric")
    stock_list1.append("Technology")
    stock_list1.append("Battery")
    stock_list1.append("Batteries")
    stock_list1.append("Twitter")
    stock_list1.append("Powered")
    stock_list1.append("Model Y")
    stock_list1.append("Model S")
    stock_list1.append("Star Link")
    stock_list1.append("Model 3")
    stock_list1.append("Model X")
    stock_list1.append("openai")
    stock_list1.append("AI")
    stock_list1.append("Science")
    stock_list1.append("Technology")
    stock_list1.append("Falcon")
    stock_list1.append("Moon")
    stock_list1.append("Rocket")
    stock_list1.append("Nasa")
    stock_list1.append("Engine")
    stock_list1.append("hyperloop")
    stock_list1.append("jet")
    stock_list1.append("physics")
    stock_list1.append("solar")
    stock_list1.append("solar city")
    stock_list1.append("solar panel")
    stock_list1.append("photocell")

    scanning()

    list_of_headlines = []

    def display_headlines():
        now = datetime.now()
        global date_time
        date_time = now.strftime("%H:%M:%S %m/%d/%Y")
        for cnn_headline in cnn_headlines:
            for stonk in stock_list1:
                if stonk in cnn_headline.text:
                    #make a list to add the headlines, so that I can print them or add them to the csv
                    list_of_headlines.append(cnn_headline.text.replace(",","")+" "+","+tsla_price.text+" "+","+date_time)
                    #print(cnn_headline.text)
        for forbes_headline in forbes_headlines:
            for stonk2 in stock_list1: 
                if stonk2 in forbes_headline.text:
                    list_of_headlines.append(forbes_headline.text.replace(",","")+" "+","+tsla_price.text+" "+","+date_time)
                    #print(forbes_headline.text)
        for bloomberg_headline in bloomberg_headlines:
            for stonk3 in stock_list1: 
                if stonk3 in bloomberg_headline.text:
                    list_of_headlines.append(bloomberg_headline.text.replace(",","")+" "+","+tsla_price.text+" "+","+date_time)
                    #print(bloomberg_headline.text)
        for MW_headline in MW_headlines:
            for stonk4 in stock_list1: 
                if stonk4 in MW_headline.text:
                    list_of_headlines.append(forbes_headline.text.replace(",","")+" "+","+tsla_price.text+" "+","+date_time)
                    #print(forbes_headline.text)
        for WSJ_headline in WSJ_headlines:
            for stonk5 in stock_list1: 
                if stonk5 in WSJ_headline.text:
                    list_of_headlines.append(WSJ_headline.text.replace(",","")+" "+","+tsla_price.text+" "+","+date_time)
                    #print(WSJ_headline.text)
    display_headlines()
    with open('headline_logs.csv', 'a') as f_object:
        writer_object = writer(f_object)
        for i in list_of_headlines[0:]:
            writer_object.writerow([i])
        f_object.close()




scrape_logger()
print("done1")
time.sleep(240)
print("done1")
scrape_logger()
print("done1")
time.sleep(240)
print("done2")
scrape_logger()
time.sleep(240)
print("done3")
scrape_logger()
time.sleep(240)
print("done4")
scrape_logger()
time.sleep(240)
print("done5")
scrape_logger()
time.sleep(240)
print("done6")
scrape_logger()
time.sleep(240)
print("done7")
scrape_logger()
time.sleep(240)
print("done8")
scrape_logger()
time.sleep(240)
print("done9")
scrape_logger()
time.sleep(240)
print("done0")
scrape_logger()
time.sleep(240)
print("done11")
scrape_logger()
time.sleep(240)
print("done12")
scrape_logger()
time.sleep(240)
print("done13")
scrape_logger()
time.sleep(240)
print("done14")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done20")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done33")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done44")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done55")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done60")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done65")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done77")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done79")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
scrape_logger()
time.sleep(240)
print("done")
time.sleep(240)
print("done80")
scrape_logger()
time.sleep(240)
print("done")
time.sleep(240)
print("done80")
scrape_logger()
time.sleep(240)
print("done")
time.sleep(240)
print("done80")
scrape_logger()
time.sleep(240)
print("done")
time.sleep(240)
print("done80")
scrape_logger()
time.sleep(240)
print("done")
time.sleep(240)
print("done80")
scrape_logger()
time.sleep(240)
print("done")
time.sleep(240)
print("done80")
scrape_logger()
time.sleep(240)
print("done")
time.sleep(240)
print("done80")
scrape_logger()
time.sleep(240)
print("donehhhhh")
time.sleep(240)
print("done80")
scrape_logger()
time.sleep(240)
print("done")



#try:
#    while True:
#        scrape_logger()
#        time.sleep(240)
#except KeyboardInterrupt:
#    pass
#Adding sleep delay to prevent being IP blocked for too many https requests


