#!/usr/bin/env python3
"""
Inserts a new doc.
"""


from pymongo import MongoClient
from bson.objectid import ObjectId

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new doc into a mongodb collection
    based on key word args.
    """
    output = mongo_collection.insert_one(kwargs)

    return result.inserted_id
