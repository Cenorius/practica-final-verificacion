from lettuce import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

@step(u'I fill the input text "([^"]*)"')
def fill_input(step, text):
    world.browser = webdriver.Chrome()
    world.browser.get("http://localhost:5000")
    try:
        i = world.browser.find_element_by_id("textfield")
        i.click()
        i.send_keys(text)
    except AssertionError as e:
        world.browser.quit()

@step(u'I click the Execute button')
def click_execute(step):
    try:
        i = world.browser.find_element_by_id("execute")
        i.click()
    except AssertionError as e:
        world.browser.quit()

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

@step(u'An error message appears')
def check_error_too_large(step):
    try:
        i = world.browser.find_element_by_id("message")
        assert "Max length is 100" == i.text
    except AssertionError as e:
        print e
    world.browser.quit()

@step(u'The input field is empty')
def check_input_text_dissapeared(step):
    try:
        i = world.browser.find_element_by_id("textfield")
        assert "" == i.text
    except AssertionError as e:
        print e
    world.browser.quit()

@step(u'Nothing happens')
def check_no_change(step):
    try:
        i = world.browser.find_element_by_id("message")
        assert "" == i.text
    except NoSuchElementException as e:
        pass
    world.browser.quit()