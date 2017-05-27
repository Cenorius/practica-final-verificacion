#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import unicodedata
from unidecode import unidecode

def remove_stop_words(words):
    """Remove Spanish stop words from a given text"""

    if not isinstance(words, list):
        raise TypeError('Argument is not a list')
    else:
        for i in words:
            if not isinstance(i, basestring):
                raise TypeError('Argument in list is not a string')

    stopwords = [u'son', u'estar\xe1', u'estadas', u'tengamos', u'hubieras', u'sentidos', u'nuestra', u'teng\xe1is', u'\xe9l', u'tuvi\xe9semos', u'estos', u'tuvimos', u'tuviste', u'nuestro', u'otro', u'tuvieron', u'antes', u'le', u'han', u'la', u'estar\xedamos', u'lo', u'estar\xedas', u'tu', u'ten\xedamos', u'quienes', u'otra', u'hubi\xe9semos', u'hay', u'suyas', u'tendr\xe9', u'ti', u'estar', u'te', u'ten\xe9is', u'habr\xedas', u'tendr\xe1', u'porque', u'estuvimos', u'ser\xedais', u'estaba', u'esa', u'yo', u'\xe9ramos', u'ya', u'cuando', u'nada', u'de', u'est\xe1is', u'tuyos', u'hayan', u'tendr\xe9is', u'estuve', u'algunos', u'hayas', u'tanto', u'qu\xe9', u'seas', u'vosostros', u'm\xeda', u'tuvieras', u'nos', u'hubimos', u'est\xe9is', u'estoy', u'estaremos', u'hubieran', u'una', u'tuvieran', u'estar\xe9is', u'somos', u'fu\xe9semos', u'desde', u'sentida', u'habr\xe9', u'nosotras', u'estados', u'sentido', u'habr\xe1', u'el', u'fuera', u'en', u'habr\xeda', u'esos', u'tendr\xe1n', u'otras', u'habr\xe9is', u'ten\xedas', u'fuesen', u'fue', u'hubieseis', u'tenida', u'soy', u'fueseis', u'seamos', u'hube', u'sea', u'tendr\xedamos', u'estamos', u'todo', u'es', u'eres', u'estad', u'tuya', u't\xfa', u'tuvieseis', u'fueses', u'hab\xedas', u'm\xedas', u'tenido', u'muy', u'tuyo', u'algunas', u'poco', u'ese', u'haya', u'sus', u'estas', u'sobre', u'ser\xedamos', u'eso', u'hab\xedais', u'tened', u'estar\xe9', u'era', u'fuerais', u'habr\xedan', u'estuvieran', u'tienen', u'fuiste', u'tuvo', u'tus', u'fu\xe9ramos', u'estar\xedais', u'les', u'que', u'como', u'estuvieras', u'habido', u'tengan', u'tendr\xe1s', u'tenidas', u'ser\xedas', u'estar\xe1s', u'estuvierais', u'ten\xeda', u'hab\xeda', u'estuvo', u'eras', u'estuviera', u'estuvisteis', u'tuvierais', u'o', u'ser\xe1s', u'est\xe1bamos', u'tambi\xe9n', u'ser\xe1n', u'nosotros', u'algo', u'quien', u'fui', u'os', u'ser\xe9is', u'uno', u'hab\xedan', u'hubiera', u'habiendo', u'est\xe1', u'teniendo', u'fuisteis', u'por', u'est\xe9', u'durante', u'mucho', u'suya', u'donde', u'estuvieron', u'tendremos', u'erais', u'ante', u'tuvisteis', u'otros', u'estaban', u'suyo', u'tienes', u'fueron', u'tenemos', u'tuvieses', u'contra', u'esas', u'estado', u'pero', u'est\xe9s', u'estemos', u'est\xe9n', u'los', u'estabas', u'nuestros', u'se\xe1is', u'est\xe1s', u'ellos', u'tuvi\xe9ramos', u'estar\xe1n', u'fueran', u'suyos', u'habidos', u'hubiese', u'tendr\xedais', u'm\xe1s', u'vuestros', u'm\xedos', u'estabais', u'para', u'fuese', u'fuimos', u'estar\xedan', u'tendr\xedas', u'fueras', u'estuvieseis', u'tendr\xedan', u'vuestro', u'vuestra', u'ha', u'ten\xedais', u'he', u'me', u'has', u'hubo', u'seremos', u'hab\xe9is', u'hubi\xe9ramos', u'mi', u'tengo', u'est\xe1n', u'ten\xedan', u'sintiendo', u'un', u'del', u'hemos', u's\xed', u'tuviera', u'tengas', u'sean', u'habr\xedais', u'este', u'unos', u'esta', u'habr\xe1n', u'estando', u'eran', u'esto', u'al', u'hayamos', u'hab\xedamos', u'estuviese', u'hay\xe1is', u'hubieses', u'sois', u'tenidos', u'tuviese', u'habr\xe1s', u'tenga', u'ni', u'tuviesen', u'no', u'estuvieses', u'ellas', u'sentidas', u'tiene', u'habr\xedamos', u'estuviesen', u'cual', u'nuestras', u'mis', u'sin', u'todos', u'vosostras', u'hubisteis', u'tuyas', u'habremos', u'tuve', u'hubiste', u'ella', u'sentid', u'hubierais', u'hubieron', u'estada', u'siente', u'ser\xeda', u'estar\xeda', u'las', u'a', u'vuestras', u'estuvi\xe9ramos', u'e', u'entre', u'habida', u'm\xed', u'ser\xedan', u'muchos', u'm\xedo', u'su', u'hasta', u'estuvi\xe9semos', u'hubiesen', u'ser\xe1', u'y', u'habidas', u'tendr\xeda', u'con', u'estuviste', u'se', u'ser\xe9']

    useful_words = []

    for i in words:
        if not isinstance(i, unicode):
            i = unicode(i, "utf-8", "ignore")
        word = unidecode(i).lower()
        if word not in stopwords:
            useful_words.append(word)

    return useful_words

def remove_digits(text):
    """Remove digits from given text"""

    if not isinstance(text, basestring):
        raise TypeError('Argument is not a string')

    return ''.join([i for i in text if not i.isdigit()])

def remove_punctuation(text):
    """Remove all punctuation signs from a given text"""

    if not isinstance(text, basestring):
        raise TypeError('Argument is not a string')

    if not isinstance(text, unicode):
        text = unicode(text, "utf-8")
    text = ''.join((c for c in unicodedata.normalize('NFD', text)\
    if unicodedata.category(c) != 'Mn'))
    return re.findall(r'\w+', text, flags=re.UNICODE | re.LOCALE)

def sort_by_times(words):
    """Obtains occurences of each word in a list or pairs
    (word, occurences) sorted by occurences."""

    if not isinstance(words, list):
        raise TypeError('Argument is not a list')
    else:
        for i in words:
            if not isinstance(i, basestring):
                raise TypeError('Argument in list is not a string')

    unordered = [[x, words.count(x)] for x in set(words)]
    return sorted(unordered, key=lambda x: x[1])

def process(text):
    """Processes the text and returns an ordered list of words from it"""

    if not isinstance(text, basestring):
        raise TypeError('Text must be a valid string')

    text = remove_digits(text)
    text = remove_punctuation(text)
    text = remove_stop_words(text)
    text = sort_by_times(text)
    return text

def convert_caps(text):
    """Converts all uppercase characters to lowercase"""
    return text.lower()


