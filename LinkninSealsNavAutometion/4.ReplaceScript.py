#  Copyright (c) 2020.
#  Version : 1.0.1
#  !/usr/bin/env python
#   coding: utf-8


from selenium import webdriver
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("chromedriver.exe",
                          chrome_options=options)
driver.implicitly_wait(5)  # seconds

# What will be searched

# Time waiting for page
waiting_for_page = 10

driver.get("https://www.linkedin.com/")

'''f = open("user.txt", "r")
data = f.read()
username = str(data).split("\n")[0]
password = str(data).split("\n")[1]
'''

# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')

driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
time.sleep(1)

driver.find_element_by_class_name("sign-in-form__submit-button").click()
time.sleep(waiting_for_page)


# No 2 : Change
# #Replace this with the link of your list
url = "https://www.linkedin.com/sales/lists/people/6700717890691194880?sortCriteria=CREATED_TIME"

driver.get(url)
time.sleep(waiting_for_page)

try:
    pages = int(driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[
                    -1].text.split("…")[-1])
except:
    pages = 1

for i in range(pages):

    people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
    people = people[1:]

    aux_count = 0
    p = 0
    before = 0

    while p < len(people):



        people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        people = people[1:]

        if before != p:
            driver.execute_script("window.scrollTo(0, {})".format(aux_count))

        before = p

        time.sleep(1)

        people[p].find_elements_by_tag_name("button")[-1].click()

        time.sleep(2)

        aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")

        do_anything = True

        #List from where you wanna remove users
        list_to_remove = "Lista de leads de Pedro"


        #List to add removed users
        list_to_add = "Shushen"

        for m in range(len(aux)):
            # No 3 : Change
            # Change to "Connect"
            if "Pending" in aux[m].text:
                do_anything = True
                break


        if do_anything:
            for m in range(len(aux)):
                # No 3 : Change
                # Change to "Add to another list"
                if "Adicionar a outra lista" in aux[m].text:
                    aux[m].click()
                    time.sleep(3)


                    cont = driver.find_element_by_class_name("entity-lists-ta__ta-container")

                    btns = cont.find_elements_by_tag_name("button")

                    #Remove from list
                    for b in btns:
                        if list_to_remove in b.text:
                            b.click()

                    time.sleep(2)
                    mn = driver.find_element_by_class_name("entity-lists-ta__unselected-menu")
                    aux_btns = mn.find_elements_by_tag_name("button")

                    for xua in aux_btns:
                        if list_to_add in xua.text:
                            xua.click()



                    time.sleep(1)
                    driver.find_element_by_class_name("edit-entity-lists-modal__save-btn").click()
                    p -= 1
                    break

        driver.find_element_by_id("content-main").click()
        time.sleep(2)
        aux_count += 80
        p += 1

    try:
        driver.find_element_by_class_name("search-results__pagination-next-button").click()
    except:
        pass
    time.sleep(10)


