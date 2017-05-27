from lettuce import *
from selenium import webdriver

@step(u'I click the Reset button')
def click_reset(step):
    try:
        i = world.browser.find_element_by_id("clear")
        i.click()
    except AssertionError as e:
        world.browser.quit()
