import pyautogui as pg
import time
import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
browser = webdriver.Chrome("/home/rushaan/PycharmProjects/automation/chromedriver",desired_capabilities=d)
browser.get("https://monkeytype.com")
browser.execute_script("document.body.style.zoom = '150%';")
browser.execute_script("arguments[0].click();",browser.find_element_by_class_name("acceptAll"))
time.sleep(5.5)

def getText():
    browser.execute_script("console.log(document.body.innerHTML);")
    hur = ""
    logs = browser.get_log("browser")
    for i in logs:
        hur += str(i)

    regex = re.compile(r"letter>\w")
    text = hur.replace("class=\\\\\"word\\\\\">", "letter>0")
    letters = regex.findall(text)
    totype = ""
    for i in range(len(letters)):
        totype += str(letters[i]).replace("letter>", "").replace("0", " ")
    return totype

pg.write(getText(),interval=0.04)
pg.write(getText(),interval=0.04)