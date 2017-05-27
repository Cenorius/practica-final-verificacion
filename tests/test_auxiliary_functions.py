#!/usr/bin/python
# -*- coding: utf-8 -*-

import mongomock


def get_fake_collection():
    """
    Creates and returns a faked collection for mongoDB
    """

    m = mongomock.MongoClient()
    return m['testing'].collection
