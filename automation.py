from selenium  import webdriver

chrome_browser = webdriver.Chrome()


chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
output_message = chrome_browser.find_element_by_id('display')

user_message.clear()  
user_message.send_keys('Automated Input')
show_message_button.click()
assert 'Automated Input' in output_message.text
print(output_message.get_attribute('innerHTML'))

chrome_browser.close()