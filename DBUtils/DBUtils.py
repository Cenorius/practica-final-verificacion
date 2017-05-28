#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import errors

QUERY_GET_WORDS_FROM_DATE=[{"$match":{"date":"?"}},{"$project":{"words":1}},{"$unwind":"$words"},{"$group":{"_id":"$words.word","count":{"$sum":"$words.apariciones"}}},{"$sort":{"count":-1}}]
QUERY_GET_WORDS_MOST_USED_FROM_DATE=[{'$match':{"date":"?"}},{'$project':{"words":1}},{'$unwind':"$words"},{'$group':{"_id":"$words.word","count":{"$sum":"$words.apariciones"}}},{"$sort":{"count":-1}},{'$limit':5}]

    
class DBUtils(object):
    # protocol = 'mongodb'
    # ip_address = '127.0.0.1'
    # port = 27017
    # mongo_db_name = 'verificacion'

    def __init__(self, collection):
        self.collection = collection

    def check_args_type(self, args):
        if isinstance(args, (list, dict)):
            return True
        return False

    def query_db(self):
        query_results = []
        [query_results.append(i) for i in self.collection.find({}, {'_id': False})]
        return query_results

    def insert_words(self,date,title,words):
        result=None
        if self.exists_article_in_db(title,date) is False:
            result= self.collection.save({"date":date,"articles":[{"title":title,"words":{words}}]})

        return result is not None
    
    def get_words_from_date(self,date):
        result=[]

        iterator=self.collection.aggregate([{"$match":{"date":date}},{"$project":{"words":1}},{"$unwind":"$words"},{"$group":{"_id":"$words.word","count":{"$sum":"$words.apariciones"}}},{"$sort":{"count":-1}}])

        for e in iterator:
            result.append(e)
        return result

    def exists_article_in_db(self,title,date):
        result=self.collection.find_one({'date':date,'title':title})
        return result is not None
    
    def exists_in_db(self, args):
        if self.check_args_type(args):
            return self.collection.find_one({'text': args})
        else:
            raise Exception("Invalid argument")

    def store_in_db(self, args):
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
