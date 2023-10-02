from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(chrome_options)

chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

assert "Selenium Easy" in chrome_browser.title

show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
print(show_message_button.get_attribute('innerHTML'))

assert "Show Message" in chrome_browser.page_source
input_text = chrome_browser.find_element(By.ID, "user-message")
input_text.clear()
input_text.send_keys("Hello World")

show_message_button.click()

output_message = chrome_browser.find_element(By.ID, "display")
assert "Hello World" in output_message.text

chrome_browser.close()
