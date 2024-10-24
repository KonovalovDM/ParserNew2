from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random

import time
# С помощью time мы можем делать задержки в программе

browser = webdriver.Firefox()  # Firefox(),
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")
# assert "Википедия" in browser.title
# time.sleep(2)

hatnotes = []

for element in browser.find_elements(By.TAG_NAME, "div"):
# Что бы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

print(hatnotes)
hatnotes = random.choice(hatnotes)
link = hatnotes.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)


# paragraphs = browser.find_elements(By.TAG_NAME,"p")
# for paragraph in paragraphs:
#    print(paragraph.text)
#    input()

# serch_box = browser.find_element(By.ID,"searchInput")
# serch_box.send_keys("Солнечная система")
# time.sleep(2)
# serch_box.send_keys(Keys.RETURN)
# time.sleep(5)
# a = browser.find_element(By.LINK_TEXT,"Солнечная система").click()
# time.sleep(5)
# browser.quit()  # закрываем браузер

# browser.save_screenshot("dom.png")
# time.sleep(4) # задержка в 15 секунд

# browser.get("https://en.wikipedia.org/wiki/Selenium")
# browser.save_screenshot("selenium.png")
# time.sleep(3)
# browser.refresh()
# time.sleep(5)

#browser.quit()  # закрываем браузер
