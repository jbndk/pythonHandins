import urllib.request
from selenium import webdriver
import bs4
import json
import re
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://www.cphbusiness.dk'
edc_url = 'https://www.edc.dk'


def edc_interaction(municipal):
    browser = webdriver.Chrome()
    browser.get(edc_url)
    browser.implicitly_wait(5)
    button_cookies = browser.find_element_by_xpath("//div[@id='coiPage-1']/div[2]/div/button[3]")
    button_cookies.click()
    input_area = browser.find_element_by_id('TextBoxSearch')
    input_area.send_keys(municipal)
    dropdown_type = browser.find_element_by_xpath('//*[@id="form1"]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/a')
    dropdown_type.click()
    checkbox_type = browser.find_element_by_xpath('//*[@id="form1"]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/span[1]')
    checkbox_type.click()
    button_search = browser.find_element_by_id('ContentContentPlaceHolder_MainContentPlaceHolder_ContentAreaNewFrontpage_ctl00_ctl02_ctl00_ctl00_ctl00_ctl01_ctl00_buttonSearch')
    button_search.click()
    browser.find_element_by_xpath('//*[@id="ContentContentPlaceHolder_MainContentPlaceHolder_'
                                  'ResultSortingAndItemsPerPage_DropDownListItemsPerPage_chosen"]').click()
    browser.find_element_by_xpath('//*[@id="ContentContentPlaceHolder_MainContentPlaceHolder_'
                                  'ResultSortingAndItemsPerPage_DropDownListItemsPerPage_chosen"]/div/ul/li[4]').click()
    browser.implicitly_wait(5)
    this_url = browser.current_url
    print(this_url)
    return this_url


def get_elements(element_url):
    sauce = urllib.request.urlopen(element_url).read()
    soup = bs4.BeautifulSoup(sauce, 'lxml')

    prices = soup.select('div[class=propertyitem__price] > strong')
    pxs = []

    for node in prices:
        px = re.sub(r'\D', '', node.text)
        pxs.append(px)
    print(pxs[0])
    house_data = soup.find_all('div', {'class': 'propertyitem__wrapper'})
    result = []

    def conv_str(s):
        num_one = filter(str.isdigit, s)
        num_two = "".join(num_one)
        return int(num_two)

    for h in house_data:
        sample = h.find_all("th")
        sample = [ele.text.strip() for ele in sample]
        sample2 = h.find_all("td")
        sample2 = [ele.text.strip() for ele in sample2]
        vals = [conv_str(s) for s in sample2]
        res = {sample[i]: vals[i] for i in range(len(sample))}
        result.append(res)

    df = pd.DataFrame(result)
    df['Pris'] = pxs

    print(df)


    '''
    sales_periods = []
    for p in sales_periods_raw:
        period = re.sub("[^0-9]", "", str(p)) 
        print("This period: " + period)
        sales_periods.append(period)

    prices = []
    for p in prices_raw:
        price = re.sub("[^0-9]", "", str(p))
        prices.append(price)

    house_dict = zip(sales_periods, prices)

    for i in house_dict:
        print(i)
'''


e_url = edc_interaction("Næstved")
get_elements(e_url)

#print(re.sub("[^0-9]", "", "sdkjh987978asd098as0980a98sd"))
