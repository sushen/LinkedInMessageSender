#  Copyright (c) 2020.
#  Version : 1.0.1
#  !/usr/bin/env python
#   coding: utf-8


from selenium import webdriver
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains

#No 1 : Change
#Message to send when connecting
message_to_connect = [
    "Hello Sir, \nI am serving International Organization for more than three years.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade.",
    "Hello Sir, \nI am working with UNDP base organization for more than three years.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade.",
    "Hello Sir, \nI am serving International Diplomate  for more than three years.my office is in Gulshan 2 near the Unicef hartal office.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade."
]

#email = "sushenbiswasaga@gmail.com"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("D:\Project\Python Tutorials Repo\LinkedInMessageSender\chromedriver.exe", chrome_options=options)
driver.implicitly_wait(5)  # seconds

#What will be searched

#Time waiting for page
waiting_for_page = 10



driver.get("https://www.linkedin.com/")

# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')


driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
time.sleep(1)

driver.find_element_by_class_name("sign-in-form__submit-button").click()
time.sleep(waiting_for_page)


#No 2 : Change
# #Replace this with the link of your list
url = "https://www.linkedin.com/sales/lists/people/6709634433944813568?sortCriteria=CREATED_TIME"

driver.get(url)
time.sleep(waiting_for_page)

try:
    pages = int(driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split("…")[-1])
except:
    pages = 1



for i in range(pages):

    people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
    people = people[1:]

    aux_count = 0
    
    for p in range(len(people)):

        people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        people = people[1:]

        driver.execute_script("window.scrollTo(0, {})".format(aux_count))

        time.sleep(1)

        people[p].find_elements_by_tag_name("button")[-1].click()

        time.sleep(2)

        aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")

        for m in range(len(aux)):
            # No 3 : Change
            # Change to "Connect"
            if "Connect" in aux[m].text:
                aux[m].click()
                time.sleep(1)

                driver.find_element_by_id("connect-cta-form__invitation").send_keys(random.choice(message_to_connect))
                time.sleep(2)


                # driver.find_element_by_id("connect-cta-form__email").send_keys(email)
                # time.sleep(1)

                driver.find_element_by_class_name("connect-cta-form__send").click()

                break

            time.sleep(2)

        driver.find_element_by_id("content-main").click()

        aux_count += 80

    try:
        driver.find_element_by_class_name("search-results__pagination-next-button").click()
    except:
        pass
    time.sleep(10)


