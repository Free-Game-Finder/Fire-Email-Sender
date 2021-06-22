from enum import Flag
from flask_pymongo import pymongo
import os


class database:
    def __init__(self):
        self.db = None
        self.users = None


def db_connect():
    database.db = pymongo.MongoClient(os.environ.get("APP_DB"))
    database.users = database.db.fgn.users


def db_email_dict(store):
    return list(database.users.find({store: True, "notify_email": True}))


def db_email_list(store):
    emails = []
    for obj in db_email_dict(store):
        emails.append(obj['email'])
    return emails
