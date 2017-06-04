# -*- coding: utf-8 -*-
from lettuce import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


@step(u'Then I see a list of articles with titles "([^"]*)" and words "([^"]*)"')
def check_list_of_words(step,titles,words):

    # Setup
    words_per_article = words.split(":")[:-1] #Erase last one
    articles = titles.split("\\")[:-1]

    if len(articles) != len(words_per_article):
        world.browser.quit()
        raise Exception('Number of articles and wordlist are not the same')

    # Check each article
    try:
        articles_read_titles = world.browser.find_elements_by_tag_name("h3")

        for i,article in enumerate(articles):
            if article != articles_read_titles[i].text:
                raise Exception('Titles do not match')
            
            # Check each word
            words_list = world.browser.find_element_by_xpath("//ul[@class='"+str(i+1)+"']")
            words_for_this_article = words_list.find_elements_by_tag_name("li")

            supposed_words = words_per_article[i].split(",")
            for word in words_for_this_article:
                if word.text not in supposed_words:
                    raise Exception('Words or count do not match: '+word.text)

    except Exception as e:
        world.browser.quit()
        raise e

    world.browser.quit()
