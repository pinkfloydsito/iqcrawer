import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

USERNAME = os.getenv("SIGAT_USER")
PASSWORD = os.getenv("PASSWORD")
SEMANA = os.getenv("SEMANA")
FINCA = os.getenv("FINCA")


WAIT_TIME = 20

browser = webdriver.Chrome(executable_path=r"/usr/bin/chromedriver")
wait = WebDriverWait(browser, 10)
browser.get('http://sigat.procesos-iq.com')

password = browser.find_element_by_name('password')
password.send_keys(PASSWORD)
username = browser.find_element_by_name('username')
username.send_keys(USERNAME)
password.send_keys(Keys.RETURN)

""" We wait until it is loaded """
element = WebDriverWait(browser, 10).until(
        EC.title_is(("Sigat | Dashboard"))
    )

""" Logged In """
browser.title
finca = browser.find_element_by_id('client')
finca.click()

try:
    WebDriverWait(browser, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='{}']".format(FINCA))))
except (TimeoutException):
    print('skip this')

finca.find_element_by_xpath("//option[@value='{}']".format(FINCA)).click()

browser.implicitly_wait(WAIT_TIME)  # seconds

save_btn = browser.find_element_by_xpath("//button[text()='Guardar y Continuar']")
browser.execute_script("arguments[0].click();", save_btn)
# save_btn.click()

""" We wait until it is loaded """
browser.implicitly_wait(WAIT_TIME)  # seconds
semana = browser.find_element_by_id('semana')

"""
Here we change the week
"""
semana.find_element_by_xpath("//option[@value='{}']".format(SEMANA)).click()
browser.implicitly_wait(WAIT_TIME) # seconds

send_btn = browser.find_element_by_xpath("//button[@class='btn green']")

""" The report is generated """
browser.execute_script("arguments[0].click();", send_btn)
