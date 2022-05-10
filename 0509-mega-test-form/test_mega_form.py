from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging

URL = 'http://selenium.oktwebs.training360.com/simplevalidation.html'

driver = ChromeDriverManager().install()
browser = webdriver.Chrome(driver)
browser.get(URL)


# create a list of elements to manipulate
elements = {}
# add the single text area
elements['test-random-textarea'] = browser.find_element_by_id('test-random-textarea')

# add all input items to the list referenced by their id
for element in browser.find_elements_by_tag_name('input'):
    elements[element.get_property('id')] = element
# add all select items to the list referenced by their id
for element in browser.find_elements_by_tag_name('select'):
    elements[element.get_property('id')] = element

print(elements.keys())
print(len(elements))
browser.quit()
