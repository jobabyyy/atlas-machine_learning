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
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_count} documents with method=GET and path=/status")
