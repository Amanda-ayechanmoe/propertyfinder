from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas

def extract_data():
    driver = webdriver.Chrome("/Users/moeamanda/Downloads/chromedriver_mac_arm64/chromedriver")
    url = "https://www.99.co/singapore/rent?listing_type=rent&map_bounds=1.005307%2C103.497799%2C1.602649%2C104.161904&page_num=1&page_size=35&path=%2Fsingapore%2Frent&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&radius_max=1000&rental_type=unit&show_cluster_preview=true&show_description=true&show_internal_linking=true&show_meta_description=true&show_nearby=true&zoom=11"
    driver.get(url)

    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//div[@class="SearchPagination"]')))
    finally:
        page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html')
    item = soup.find_all('div', {"class":"_17qrb WgBDo"})

    print(len(item))
    prepare_data(item)

def prepare_data(item):
    list = []
    for listing in item[:10]:
        #for grip in listing.find_all('div', {"class":"_2J3pS _1gyCD"}):
        for card in listing.find_all('div', {"class": "TaGB0"}):
            print(card.find('a', {"class": "_3Ajbv _30I97 _1vzK2"}).text)
            if(card.find('p', {"class": "dniCg _1RVkE _2rhE- _1c-pJ"})):
                print(card.find('p', {"class": "dniCg _1RVkE _2rhE- _1c-pJ"}).text)
            if(card.find('li', {"class": "_3WG9R _3L5OV"})):
                print(card.find('li', {"class": "_3WG9R _3L5OV"}).text)
            for bedbath in card.find_all('span', {"class":"cUjn9"}):
                if(bedbath.find('li', {"class":"_1x-U1"})):
                    print(bedbath.find('li', {"itemprop":"numberOfBedrooms"}).text)
                    print(bedbath.find('li', {"itemprop": "numberOfBathroomsTotal"}).text)
                    print(bedbath.find('li', {"itemprop": "floorSize"}).text)
            if (card.find('li', {"itemprop": "price"})):
                print((card.find('li', {"itemprop": "price"})).text)
            print('-------------------')

    #print(d)

