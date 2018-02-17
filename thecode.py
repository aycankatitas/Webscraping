# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:44:39 2017

@author: aycankatitas
Description: Python code for webscraping NewsBank with selenium
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import random
import time
import csv
import codecs
from contextlib import contextmanager


f = open('ma.csv')
csv_f = csv.reader(f)
start_line = 1
end_line = 6
lines = f.readlines()[start_line:end_line]

# CREATE LISTS FROM CSV FILE 

company_names = []
company_day1= []
company_month1 = []
company_year1 = []
company_day2 = []
company_month2 = []
company_year2 = []
for line in lines:
    stripped_line = line.strip()
    row = stripped_line.split(",")
    company_names.append(row[0])
    company_day1.append(row[1])
    company_month1.append(row[2])
    company_year1.append(row[3])
    company_day2.append(row[4])
    company_month2.append(row[5])
    company_year2.append(row[6])
while company_names != []:
    company_name_search = (company_names[0])
    company_day1_search= (company_day1[0])
    company_day1.remove(company_day1_search)
    company_day1_search = str(company_day1_search)
    company_month1_search = (company_month1[0])
    company_month1.remove(company_month1_search)
    company_month1_search = str(company_month1_search)
    company_year1_search = (company_year1[0])
    company_year1.remove(company_year1_search)
    company_year1_search = str(company_year1_search)
    company_day2_search= (company_day2[0])
    company_day2.remove(company_day2_search)
    company_day2_search = str(company_day2_search)
    company_month2_search = (company_month2[0])
    company_month2.remove(company_month2_search)
    company_month2_search = str(company_month2_search)
    company_year2_search = (company_year2[0])
    company_year2.remove(company_year2_search)
    company_year2_search = str(company_year2_search)
    company_date_search = (company_month1_search + " " + company_day1_search + ", " + company_year1_search + " - " + company_month2_search + " " + company_day2_search + ", " + company_year2_search)


    path_to_chromedriver = '/Users/aycankatitas/Downloads/chromedriver' #change the path to your own Chrome driver
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)
    browser.implicitly_wait(20) # seconds
    

# Open a webpage 
    url = 'http://infoweb.newsbank.com/resources/search/nb?p=AWNB'
    browser.get(url)

# Searching for all USA newspapers - first clicking North America then USA

    browser.find_element_by_xpath('//*[@id="nb-browse-table"]/tbody/tr[8]/td/a').click()

    browser.find_element_by_xpath('//*[@id="nb-browse-table"]/tbody/tr[4]/td/a').click()

## selecting Lead/First Paragraph

    mySelect = Select(browser.find_element_by_id("nbplatform-basic-search-fld0"))
    mySelect.select_by_visible_text("Lead/First Paragraph")

## Search Box 1 - Company name Acquiror + Target

    browser.find_element_by_id('nbplatform-basic-search-val0').clear() # Find the id name and write it here
    browser.find_element_by_id('nbplatform-basic-search-val0').send_keys(company_names[0])
    company_names.remove(company_name_search)

    mySelect = Select(browser.find_element_by_id("nbplatform-basic-search-fld1"))
    mySelect.select_by_visible_text("Date(s)")

    browser.find_element_by_id('nbplatform-basic-search-val1').clear() # Find the id name and write it here
    browser.find_element_by_id('nbplatform-basic-search-val1').send_keys(company_date_search)

    mySelect = Select(browser.find_element_by_id("nbplatform-basic-search-sort"))
    mySelect.select_by_visible_text("Best matches first")

    browser.find_element_by_xpath('//*[@id="nbplatform-basic-search-submit"]')
    
##CLICK SEARCH BUTTON
    browser.find_element_by_xpath('//*[@id="nbplatform-basic-search-submit"]').click()

## Number of Results 

    number_of_results = browser.find_element_by_class_name("nb-showing-result-count").text
    print (company_name_search, number_of_results)
