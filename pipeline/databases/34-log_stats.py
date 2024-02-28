#!/usr/bin/env python3
"""
Generating stats.
"""


from pymongo import MongoClient


def nginx_logs_stats():
    """
    provide stats about Ngnix logs stored in MongoDB:
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    log_collection = db['nginx']

    total_logs = log_collection.count_documents({})

    print(f"first line: {total_logs} logs where {total_logs} is the number of documents in this log_collection")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = log_collection.count_documents({"method": method})
        print(f"\t{count} logs with method={method}")

    count_stat = log_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{count_stat} logs with method=GET\npath=/status")