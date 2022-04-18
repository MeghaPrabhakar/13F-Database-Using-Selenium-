import requests
from bs4 import BeautifulSoup
import csv
import xml.etree.ElementTree as ET

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from lxml import html
import html5lib
from selenium.webdriver.common.by import By
from xml.dom import minidom
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

import codecs
import pandas as pd  # to convert the csv to excel
from openpyxl.workbook import Workbook


# import call

def file1(driver_url):  # call with the driver value
    # driver=webdriver.Chrome(executable_path='/Users/meghaprabhakar/Desktop/chromedriver')
    print('___________________________')
    # print(x)
    driver.get(driver_url)  #

    # ------------FILE1-----------#
    driver.find_element_by_xpath("//*[@id='formDiv']/div/table/tbody/tr[3]/td[3]/a").click()
    time.sleep(3)
    Element = driver.find_element_by_id('webkit-xml-viewer-source-xml')
    Element_attribute_value = Element.get_attribute('innerHTML')
    save_path_file = "form13_scraped.xml"  # file name as required
    with open(save_path_file, 'w') as f:  # save the XML into a file
        f.write(Element_attribute_value)
    tree = ET.parse('form13_scraped.xml')
    root = tree.getroot()
    xml_data_to_csv = open('out.csv', 'w')
    # df = pd.DataFrame()
    # df.to_csv('out.csv')
    csv_writer = csv.writer(xml_data_to_csv)
    dict1 = {}

    def tree_recursion(root):
        for child in root:
            if len(child.text.strip()) > 0:
                i = (child.tag.index('}'))
                dict1[child.tag[i + 1:]] = child.text
            tree_recursion(child)

    tree_recursion(root)
    # df.to_csv('out.csv')
    csv_writer.writerow(dict1.keys())
    csv_writer.writerow(dict1.values())
    time.sleep(5)


def file2(driver_url):  # pass the driver value as parameter
    # driver = webdriver.Chrome(executable_path='/Users/meghaprabhakar/Desktop/chromedriver')
    driver.get(driver_url)
    # ------------FILE2-----------#
    driver.find_element_by_xpath("//*[@id='formDiv']/div/table/tbody/tr[5]/td[3]/a").click()
    time.sleep(3)
    Element1 = driver.find_element_by_id('webkit-xml-viewer-source-xml')
    Element_attribute_value1 = Element1.get_attribute('innerHTML')
    save_path_file1 = "form13_info_scraped.xml"
    with open(save_path_file1, 'w') as f:
        f.write(Element_attribute_value1)

    tree1 = ET.parse('form13_info_scraped.xml')
    root1 = tree1.getroot()
    xml_data_to_csv1 = open('out1.csv', 'w')
    csv_writer1 = csv.writer(xml_data_to_csv1)
    dict2 = {}
    # l2=[]
    i = 1

    def tree_recursion1(root1):
        for child in root1:
            # time.sleep(2)
            if (child.text):
                if len(child.text.strip()) > 0:
                    i = (child.tag.index('}'))
                    if (child.tag[i + 1:] == 'None'):
                        dict2[child.tag[i + 1:]] = child.text
                        csv_writer1.writerow(dict2.values())
                    else:
                        dict2[child.tag[i + 1:]] = child.text
            else:
                i = (child.tag.index('}'))
                if (child.tag[i + 1:] == 'None'):
                    dict2[child.tag[i + 1:]] = child.text
                    csv_writer1.writerow(dict2.values())
                else:
                    dict2[child.tag[i + 1:]] = child.text
            tree_recursion1(child)

    tree_recursion1(root1)
    csv_writer1.writerow(dict2.keys())
    xml_data_to_csv1.close()


def control(newURL):
    x = newURL
    # x="'"+newURL+"'"
    # print('=================================================')
    # print(x)
    file1(x)
    file2(x)
    return


# control()


# ================================================================================================
driver = webdriver.Chrome(executable_path='/Users/meghaprabhakar/Desktop/chromedriver')
driver.get('https://www.sec.gov/edgar/search/#/category=custom&entityName=ford&forms=13F-HR')  # get url on the browser
driver.maximize_window()

time.sleep(2)
rowelements = len(driver.find_elements_by_xpath("//*[@id='hits']/table/tbody/tr"))
time.sleep(2)
# print(rowelements)
time.sleep(2)
colelements = len(driver.find_elements_by_xpath("//*[@id='hits']/table/tbody/tr[7]/td"))
time.sleep(2)
# print(colelements)
time.sleep(2)

driver.find_element(By.XPATH, value='//input[@id="col-cik"]').click()

time.sleep(5)
columns = len(driver.find_elements_by_xpath(".//*[@class='table']/tbody/tr[6]/td"))
rows = len(driver.find_elements_by_xpath(".//*[@class='table']/tbody/tr"))
rowelements = len(driver.find_elements_by_xpath("//*[@id='hits']/table/tbody/tr"))
print("rows - ", rows)  # rows -  3
print("columns - ", columns)  # columns -  4

with open('flatfile.csv', 'r') as f1:
    mycsv1 = csv.reader(f1)
    mycsv1 = list(mycsv1)
    print(mycsv1[0])
for row in range(1, rowelements - 1):
    value = driver.find_element_by_xpath(".//*[@class='table']/tbody/tr[" + str(row) + "]/td[5]").text
    if (value in mycsv1[0]):
        print('--------------')
        print('true')
        print(driver.find_element_by_xpath(
            ".// *[ @ id = 'hits'] / table / tbody / tr[" + str(row) + "] / td[1] / a").text)
        print(driver.find_element_by_xpath(".//*[@class='table']/tbody/tr[" + str(row) + "]/td[5]").text)
        value = driver.find_element_by_xpath(".//*[@class='table']/tbody/tr[" + str(row) + "]/td[5]").text
        driver.find_element_by_xpath(".// *[ @ id = 'hits'] / table / tbody / tr[" + str(row) + "] / td[1] / a").click()
        time.sleep(3)
        driver.find_element_by_xpath("(.//*[@class='btn btn-warning'])[2]").click()
        time.sleep(3)
        newURl = driver.window_handles[1]  # switch the control to the newly opened page
        driver.switch_to.window(newURl)
        # print(newURl)
        # print(driver.current_url)
        control(driver.current_url)  # the control function is called
        time.sleep(20)
        print('----------------------------------------------------------------------')
        # driver.back()
        # time.sleep(5)
        driver.close()
        newURL = driver.window_handles[0]  # switch the control back to the old page
        print(driver.window_handles[0])
        # print('++++++++++++++++')
        print(newURL)
        driver.switch_to.window(newURL)
        time.sleep(5)
        driver.find_element_by_xpath("(.//*[@class='btn btn-light btn-outline-dark'])").click()
        # driver.find_element_by_xpath("//*[@id='previewer']/div/div/div[3]/button")
        time.sleep(5)
        if (os.stat("out.csv").st_size == 0):
            continue
        else:
            from dataframe_concept import *

            full_info()
            full_info1()

