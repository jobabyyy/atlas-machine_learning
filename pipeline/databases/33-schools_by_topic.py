#!/usr/bin/env python3
"""
Schools By Topic.
"""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Finds school specifics that have a specific topic.
    """

    school = mongo_collection.find({"topics": topic})

    return list(school)
