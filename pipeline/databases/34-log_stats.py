#!/usr/bin/env python3
"""
Generating stats.
"""


from pymongo import MongoClient


def nginx_logs_stats():
    """
    provide stats about Ngnix logs stored in MongoDB:
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{method}: {count}")

    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} documents with method=GET and path=/status")
