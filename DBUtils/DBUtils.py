#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import errors
from datetime import datetime

    
class DBUtils(object):

    def __init__(self, collection):
        self.collection = collection

    def query_db(self):
        """
        Used only during testing
        """
        query_results = []
        [query_results.append(i) for i in self.collection.find({}, {'_id': False})]
        return query_results

    def insert_words(self,date,title,words):
        result=None

        if not isinstance(title,(str,unicode)) or not isinstance(words,list):
            raise TypeError

        if not self._is_date(date):
            raise Exception("Date format is not valid")
        try:
            if self.exists_article_in_db(title,date) is False:
                words=self._format_words(words)
                result= self.collection.save({"date":date,"title":title,"words":words})
        except:
            raise Exception("Database connection failed")

        return result is not None
    
    def _format_words(self,words):
        result=[]

        if isinstance(words,list):
            for word in words:
                result.append({"word":word[0],"count":word[1]})
        else:
            raise TypeError

        return result

    def _is_date(self,date):
        try: 
            datetime.strptime(date,"%d/%m/%Y")
            return True
        except:
            return False

    def get_words_from_date(self,date): 
        result=[]

        if not self._is_date(date):
            raise Exception("Date format is not valid")
        try:
            iterator=self.collection.aggregate([{"$match":{"date":date}},{"$project":{"words":1}},{"$unwind":"$words"},{"$group":{"_id":"$words.word","count":{"$sum":"$words.count"}}},{"$sort":{"count":-1}}])
        except:
            raise Exception("Database connection failed")
        
        for e in iterator:
            result.append(e)
        return result

    def get_words_from_article(self,date, title):
        result=[]

        if not isinstance(title,(str,unicode)):
            raise TypeError

        if not self._is_date(date):
            raise Exception("Date format is not valid")
        
        try:
            iterator=self.collection.aggregate([{"$match":{"date":date, "title":title}},{"$project":{"words":1}},{"$unwind":"$words"},{"$group":{"_id":"$words.word","count":{"$first":"$words.count"} }},{"$sort":{"count":-1}}])
        except:
            raise Exception("Database connection failed")
        
        for e in iterator:
            result.append(e)
        return result

    def exists_article_in_db(self,title,date):
        if not self._is_date(date):
            raise Exception("Date format is not valid")
        
        try:
            result=self.collection.find_one({'date':date,'title':title})
        except:
            raise Exception("Database connection failed")
        
        return result is not None

    def clean_db(self):
        self.collection.remove({})

if __name__ == "__main__":
    # Old main:
    """
    from pymongo import MongoClient
    objects = ["this", "is", "a", "test", "list"]

    client = MongoClient()
    db = client.verificacion
    coll = db.text

    client = DBUtils(coll)

    client.clean_db()

    client.store_in_db(objects)
    stored = client.query_db()

    print stored

    client.clean_db()
    """