#!/usr/bin/env python3
"""
Updating topics.
"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school doc  based on school name.
    """

    update_collection.update_many({"name": name}, {"$set": {"topics": topics}})
