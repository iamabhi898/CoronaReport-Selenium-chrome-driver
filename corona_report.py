from selenium import webdriver

PATH = "/home/abhishek/Documents/chromedriver.exe"
entry = input("Worldwide(W) or India(I) ? : \n")
driver = webdriver.Chrome(PATH)

if entry.lower() == "w":

	print("\n\n\n\n")
	driver.get("https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN:en")
	driver.implicitly_wait(10)

	country_list = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[5]/div/div/div[1]/div/div[1]')
	print(country_list.text)
	
	driver.close()

elif entry.lower() == "i":

	print("\n\n\n\n")
	driver.get('https://www.mohfw.gov.in/')
	driver.implicitly_wait(5)

	data_button = driver.find_element_by_xpath('//*[@id="site-dashboard"]/div/div/div/div/ul/li[5]/a[2]/img')
	data_button.click()

	state_list = driver.find_element_by_xpath('//*[@id="state-data"]/div/div/div/div/table')
	print(state_list.text)

	driver.close()
