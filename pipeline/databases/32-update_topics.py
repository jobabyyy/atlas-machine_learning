#!/usr/bin/env python3
"""
Updating topics.
"""


from pymongo import MongoClient


def update_topics(mongo_client, name, topics):
    """
    Updates the topics of a school doc  based on school name.
    """

    update_collection({ "name": name }, { "$set": {"topics": topics} })
