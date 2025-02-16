from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from engine.config import SeleniumConfig


#region DRIVER

def open(website, cookies):
    options = webdriver.ChromeOptions()
    SeleniumConfig.apply_options(options)
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    return driver

def change_url(driver, url):
    driver.get(url)

#endregion


#region INTERACT

def send_string(element, value):
    element.send_keys(value)

def type_string(element, value):
    for c in value:
        element.send_keys(c)
        # time.sleep(0.05 + random.uniform(0.01, 0.1))

#endregion


#region PARSE

def get_element(element, type, query):
    return element.find_element(type, query)

def get_elements(element, type, query):
    return element.find_elements(type, query)

def get_element_visible(driver, type, query, timeout = SeleniumConfig.find_element_timeout):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((type, query))
    )

def get_element_visible_by_text(driver, text):
    return WebDriverWait(driver, SeleniumConfig.find_element_timeout).until(
        EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "{text}")]'))
    )

def get_children(element):
    return element.find_elements(By.XPATH, './*')

def get_child(element, indices):
    for index in indices:
        children = get_children(element)
        if len(children) <= index:
            return None
        element = children[index]
    return element

def wait_for_element_disappear(driver, type, query):
    WebDriverWait(driver, SeleniumConfig.find_element_timeout).until(
        EC.invisibility_of_element_located((type, query))
    )

#endregion
