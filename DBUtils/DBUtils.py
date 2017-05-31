#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import errors
from datetime import datetime

QUERY_GET_WORDS_FROM_DATE=[{"$match":{"date":"?"}},{"$project":{"words":1}},{"$unwind":"$words"},{"$group":{"_id":"$words.word","count":{"$sum":"$words.apariciones"}}},{"$sort":{"count":-1}}]
QUERY_GET_WORDS_MOST_USED_FROM_DATE=[{'$match':{"date":"?"}},{'$project':{"words":1}},{'$unwind':"$words"},{'$group':{"_id":"$words.word","count":{"$sum":"$words.apariciones"}}},{"$sort":{"count":-1}},{'$limit':5}]

    
class DBUtils(object):
    # protocol = 'mongodb'
    # ip_address = '127.0.0.1'
    # port = 27017
    # mongo_db_name = 'verificacion'

    def __init__(self, collection):
        self.collection = collection

    def check_args_type(self, args):#no se usa
        if isinstance(args, (list, dict)):
            return True
        return False

    def query_db(self):#no se usa
        query_results = []
        [query_results.append(i) for i in self.collection.find({}, {'_id': False})]
        return query_results

    def insert_words(self,date,title,words):
        result=None

        if not isinstance(title,(str,unicode)) or not isinstance(words,list):
            raise TypeError

        if not self._is_date(date):
            raise Exception("Date format is not valid")
        
        if self.exists_article_in_db(title,date) is False:
            words=self._format_words(words)
            result= self.collection.save({"date":date,"title":title,"words":words})

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

        iterator=self.collection.aggregate([{"$match":{"date":date}},{"$project":{"words":1}},{"$unwind":"$words"},{"$group":{"_id":"$words.word","count":{"$sum":"$words.count"}}},{"$sort":{"count":-1}},{"$limit":10}])

        for e in iterator:
            result.append(e)
        return result

    def get_words_from_article(self,date, title):
        result=[]

        if not isinstance(title,(str,unicode)):
            raise TypeError

        if not self._is_date(date):
            raise Exception("Date format is not valid")
        
        iterator=self.collection.aggregate([{"$match":{"date":date, "title":title}},{"$project":{"words":1}},{"$unwind":"$words"},{"$group":{"_id":"$words.word","count":{"$first":"$words.count"} }},{"$sort":{"count":-1}}])

        for e in iterator:
            result.append(e)
        return result

    def exists_article_in_db(self,title,date):
        result=self.collection.find_one({'date':date,'title':title})
        return result is not None
    
    def exists_in_db(self, args):#no se usa
        if self.check_args_type(args):
            return self.collection.find_one({'text': args})
        else:
            raise Exception("Invalid argument")

    def store_in_db(self, args):#no se usa
        _id = ""
        if self.check_args_type(args):
            try:
                if self.exists_in_db(args):
                    raise Exception("data already exists in DB")
                else:
                    _id = self.collection.insert_one({'text': args}).inserted_id
                return _id
            except errors.ConnectionFailure as err:
                raise Exception(err)
        else:
            raise Exception("Invalid argument")

    def clean_db(self):
        self.collection.remove({})

if __name__ == "__main__":
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
