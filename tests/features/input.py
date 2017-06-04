from lettuce import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

@step(u'I fill the input date with "([^"]*)"')
def fill_input_date(step, date):
    world.browser = webdriver.Chrome()
    world.browser.get("http://localhost:5000")

    #date_without_slashes = date.strip('/')

    try:
        datefield = world.browser.find_element_by_id("datepicker")

        world.browser.execute_script("arguments[0].value = '"+date+"';", datefield) 

    except AssertionError as e:
        world.browser.quit()

@step(u'I click the Execute button')
def click_execute(step):
    try:
        i = world.browser.find_element_by_id("execute")
        i.click()
    except AssertionError as e:
        world.browser.quit()

@step(u'Select "([^"]*)"')
def select_option(step, option):
    if option == "muw":
        try:
            i = world.browser.find_element_by_id("source-0")
            i.click()
        except AssertionError as e:
            world.browser.quit()
    elif option == "wpa":
        try:
            i = world.browser.find_element_by_id("source-1")
            i.click()
        except AssertionError as e:
            world.browser.quit() 
    else:
        print option
        raise Exception('Invalid option to select')
        world.browser.quit() 

@step(u'An error message appears "([^"]*)"')
def check_error(step,error):
    i = world.browser.find_element_by_id("messages-container")

    if error != i.text:
        raise Exception('Error message not found or incorrect')

    world.browser.quit()

"""
@step(u'I can see the list of words "([^"]*)" with their number of appearances: "([^"]*)"')
def check_list_of_words(step, words, appearances):
    # parse words and count to list
    list_words = words.split(",")
    list_appearances = appearances.split(",")

    try:
        messages = world.browser.find_element_by_id("messages-container")
        for i, message in enumerate(messages.find_elements_by_xpath(".//*")):
            m = message.text.split(":")
            assert m[0] == list_words[i]
            assert m[1].strip() == list_appearances[i]

    except AssertionError as e:
        print e


@step(u'Nothing happens')
def check_no_change(step):
    try:
        i = world.browser.find_element_by_id("message")
        assert "" == i.text
    except NoSuchElementException as e:
        pass
    world.browser.quit()
"""