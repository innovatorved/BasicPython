#web automation usiing Selenium

from selenium import webdriver

#driver of web broweser avail in official website of selenium
browser = webdriver.Chrome('C:\\Users\\VED GUPTA\\Documents\\driver Chroma Selenium\\chromedriver')   

#website which u want to open
browser.get('https://www.google.com/')

#find anything on browser
elem = browser.find_element_by_class_name('gLFyf gsfi')




