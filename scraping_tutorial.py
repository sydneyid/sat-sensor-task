#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:38:03 2023

@author: sydneydolan
"""

#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

warnings.filterwarnings('ignore')


# url = "https://in-the-sky.org/satpasses.php?day=6&month=5&year=2023&mag=500&anysat=v0&group=1&s=&gs=gs"

url = "https://in-the-sky.org/satpasses.php?day=6&month=5&year=2023&mag=4&anysat=v0&group=1&s=&gs=gs"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Safari()
driver.get(url) 
# this is just to ensure that the page is loaded
time.sleep(5) 
  
html = driver.page_source

soup2 = BeautifulSoup(html, 'html.parser')
driver.close()



main_page = soup2.find("div", attrs = {"class":"mainpage container"}).find("div", attrs = {"class":"row"}).find("div", attrs = {"class":"col-xl-10b"}).find("div", attrs = {"class":"mainpane"}).find("div", attrs = {"class":"sat_passes"}).find("div", attrs = {"class":"sp_target"}).find("div", attrs = {"style":"padding-bottom:15px;"})    

#print(str(main_page))
for table in main_page.find_all('table'):
    print(table.get('class'))

#  Looking for the table with the classes 'wikitable' and 'sortable'
table = main_page.find('table', class_='stripy sattable')

# Defining of the dataframe
df = pd.DataFrame(columns=['Name','Start Time','Start Direction', 'Start Alt', 'End Time', 'End Direction', 'End Alt'])


checker=0
# Collecting Ddata
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    
    if(columns != []):
        # index=0
        # for c in columns:
        #     print(str(index)+'  ' + str(c))
        #     index+=1
        name = columns[0].text.strip()
        start = columns[2].text.strip()
        start_dir = columns[3].text.strip()
        start_alt = columns[4].text.strip()#[:-1]
        
        end = columns[10].text.strip()
        end_dir = columns[11].text.strip()
        end_alt = columns[12].text.strip()#[:-1]

        if df['Name'].str.contains(name).any()==False:
            # 1
        # else:
            df = df.append({'Name': name,  'Start Time': start, 'Start Direction': start_dir, 'Start Alt': start_alt, 'End Time': end, 'End Direction': end_dir, 'End Alt':end_alt}, ignore_index=True)
    #     checker+=1
        
    # if checker==5:
    #     break


df.to_csv('ListOfSatellitesFinal.csv', encoding='utf-8', index=False)
