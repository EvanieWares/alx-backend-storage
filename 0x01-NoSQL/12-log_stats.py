#!/usr/bin/env python3
"""
Module 12-log_stats

A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_database = client.logs
    nginx_collection = logs_database.nginx
    total = nginx_collection.count_documents({})
    get = nginx_collection.count_documents({"method": "GET"})
    post = nginx_collection.count_documents({"method": "POST"})
    put = nginx_collection.count_documents({"method": "PUT"})
    patch = nginx_collection.count_documents({"method": "PATCH"})
    delete = nginx_collection.count_documents({"method": "DELETE"})
    path = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
