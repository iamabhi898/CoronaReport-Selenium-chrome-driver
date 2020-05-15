from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def report(query):

    PATH = "/home/abhishek/Documents/chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    if query.lower() == 'w':
        driver.get(
            "https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN:en")
        driver.implicitly_wait(10)
        country_list = driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[5]/div/div/div[1]/div/div[1]')
        print("\n\n\n\n")
        print(country_list.text)
        driver.close()

    elif query.lower() == 'i':
        driver.get('https://www.mohfw.gov.in/')
        driver.implicitly_wait(5)

        data_button = driver.find_element_by_xpath(
            '//*[@id="site-dashboard"]/div/div/div/div/ul/li[5]/a[2]/img')
        data_button.click()
        state_list = driver.find_element_by_xpath(
            '//*[@id="state-data"]/div/div/div/div/table')
        print("\n\n\n\n")
        print(state_list.text)
        driver.close()


if __name__ == '__main__':
    entry = input("Worldwide(W) or India(I) ? : \n")
    report(entry)
    driver.close()
