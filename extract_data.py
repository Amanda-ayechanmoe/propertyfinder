from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas

def search_param(filter_list):
    url_builder_mapping = {"East-West Line":"EW9+Aljunied+MRT%2C+EW10+Kallang+MRT%2C+EW11+Lavender+MRT%2C+DT14%2FEW12+Bugis+MRT&market=residential&MRT_STATIONS%5B%5D=EW9&MRT_STATIONS%5B%5D=EW10&MRT_STATIONS%5B%5D=EW11&MRT_STATIONS%5B%5D=DT14&MRT_STATIONS%5B%5D=EW12",
                           "North-South Line":"EW24%2FNS1%2FJE5+Jurong+East+MRT%2C+NS2+Bukit+Batok+MRT%2C+NS3+Bukit+Gombak+MRT%2C+BP1%2FNS4%2FJS1+Choa+Chu+Kang+LRT%2C+JS1%2FNS4%2FBP1+Choa+Chu+Kang+MRT%2C+NS5+Yew+Tee+MRT%2C+NS7+Kranji+MRT%2C+NS8+Marsiling+MRT%2C+NS9%2FTE2+Woodlands+MRT%2C+NS10+Admiralty+MRT%2C+NS11+Sembawang+MRT%2C+NS12+Canberra+MRT%2C+NS13+Yishun+MRT%2C+NS14+Khatib+MRT%2C+NS15+Yio+Chu+Kang+MRT%2C+CR11%2FNS16+Ang+Mo+Kio+MRT%2C+CC15%2FNS17+Bishan+MRT%2C+NS18+Braddell+MRT%2C+NS19+Toa+Payoh+MRT%2C+NS20+Novena+MRT%2C+DT11%2FNS21+Newton+MRT%2C+NS22%2FTE14+Orchard+MRT%2C+NS23+Somerset+MRT%2C+CC1%2FNS24%2FNE6+Dhoby+Ghaut+MRT%2C+EW13%2FNS25+City+Hall+MRT%2C+EW14%2FNS26+Raffles+Place+MRT%2C+CE2%2FNS27%2FTE20+Marina+Bay+MRT%2C+NS28+Marina+South+Pier+MRT&market=residential&MRT_STATIONS%5B%5D=EW24&MRT_STATIONS%5B%5D=JE5&MRT_STATIONS%5B%5D=NS1&MRT_STATIONS%5B%5D=NS2&MRT_STATIONS%5B%5D=NS3&MRT_STATIONS%5B%5D=BP1&MRT_STATIONS%5B%5D=JS1&MRT_STATIONS%5B%5D=NS4&MRT_STATIONS%5B%5D=NS5&MRT_STATIONS%5B%5D=NS7&MRT_STATIONS%5B%5D=NS8&MRT_STATIONS%5B%5D=NS9&MRT_STATIONS%5B%5D=TE2&MRT_STATIONS%5B%5D=NS10&MRT_STATIONS%5B%5D=NS11&MRT_STATIONS%5B%5D=NS12&MRT_STATIONS%5B%5D=NS13&MRT_STATIONS%5B%5D=NS14&MRT_STATIONS%5B%5D=NS15&MRT_STATIONS%5B%5D=CR11&MRT_STATIONS%5B%5D=NS16&MRT_STATIONS%5B%5D=CC15&MRT_STATIONS%5B%5D=NS17&MRT_STATIONS%5B%5D=NS18&MRT_STATIONS%5B%5D=NS19&MRT_STATIONS%5B%5D=NS20&MRT_STATIONS%5B%5D=DT11&MRT_STATIONS%5B%5D=NS21&MRT_STATIONS%5B%5D=NS22&MRT_STATIONS%5B%5D=TE14&MRT_STATIONS%5B%5D=NS23&MRT_STATIONS%5B%5D=CC1&MRT_STATIONS%5B%5D=NE6&MRT_STATIONS%5B%5D=NS24&MRT_STATIONS%5B%5D=EW13&MRT_STATIONS%5B%5D=NS25&MRT_STATIONS%5B%5D=EW14&MRT_STATIONS%5B%5D=NS26&MRT_STATIONS%5B%5D=CE2&MRT_STATIONS%5B%5D=NS27&MRT_STATIONS%5B%5D=TE20&MRT_STATIONS%5B%5D=NS28"}
    search_param = ''
    for filter in filter_list:
        if filter in url_builder_mapping.keys():
            search_param = search_param+url_builder_mapping[filter]

    print(f'Inside extract_data{search_param}')
    extract_data(search_param)

def extract_data(search_param):
    # create chrome dirver using selenium
    driver = webdriver.Chrome("/Users/moeamanda/Downloads/chromedriver_mac_arm64/chromedriver")

    # URL with search filter
    url = f'https://www.propertyguru.com.sg/property-for-rent?freetext={search_param}'
    driver.get(url)
    # selenium + beautiful soup for dynamic scraping
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="listing-pagination"]')))
    finally:
        page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html')
    item = soup.find_all('div', {"row"})
    #print(item)
    item_listing = soup.find_all('div', {"class": "col-xs-12 col-sm-12 listing-description"})
    #print(item_listing)
    prepare_data(item_listing)

def prepare_data(item_listing):
    l = []
    for listing in item_listing:
        d = {}
        if len(listing.find_all("a", {"class": "nav-link"})):
            if (listing.find_all("a", {"class": "nav-link"})[0].text):
                d["Property Name"] = listing.find_all("a", {"class": "nav-link"})[0].text
            for address in listing.find_all("p", {"class": "listing-location ellipsis"}):
                d["Address"] = address.find("span").text
            for price in listing.find_all("ul", {"class": "listing-features"}):
                for price_list in listing.find_all("li", {"class": "list-price pull-left"}):
                    if (price.find("span", {"class": "currency"}) and price.find("span", {"class": "price"})):
                        d["Price"] = price.find("span", {"class": "currency"}).text + price.find("span", {
                            "class": "price"}).text
                    #if (price.find("span", {"class": "currency"})):
                        #print(price.find("span", {"class": "period"}).text)
            if (listing.find("li", {"class": "listing-availability pull-left"})):
                d["Available Date"] = listing.find("li", {"class": "listing-availability pull-left"}).text

            for features in listing.find_all("ul", {"class": "listing-features pull-left"}):
                for rooms in listing.find_all("li", {"class": "listing-rooms pull-left"}):
                    if (features.find("span", {"class": "bed"})):
                        d["Bed"] = rooms.find("span", {"class": "bed"}).text + " bed"
                    if (features.find("span", {"class": "bath"})):
                        d["Bath"] = rooms.find("span", {"class": "bath"}).text + " bath"
        if (len(d) != 0):
            l.append(d)
        export_data(l)

def export_data(l):
    df = pandas.DataFrame(l)
    print(df)
    df.to_csv("output.csv")


