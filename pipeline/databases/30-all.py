#!/usr/bin/env python3
"""
Using MongoDB for collections
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """ list all dics in the specified MongoDB collection.
    """
    docs = list(mongo_collection.find())

return docs
