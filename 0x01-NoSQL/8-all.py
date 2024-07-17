#!/usr/bin/env python3
"""
Module 8-all

List all documents in Python
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Parameters:
    - mongo_collection (pymongo): The collection object

    Returns:
    - list: All documents in the collection
    - list: An empty list if no document in the collection
    """
    return mongo_collection.find()
