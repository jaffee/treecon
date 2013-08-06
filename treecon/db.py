import pymongo
from treecon import app
import validictory
import time

schema = app.config["THING_SCHEMA"]


def validate_add_defaults(data, schema):
    validictory.validate(data, schema)


thing_c = pymongo.Connection('localhost')[app.config['DBNAME']][app.config['COLLNAME']]

def get_item(the_id):
    return thing_c.find_one({'id': the_id})


def extract_items(key, value):
    cursor = thing_c.find({key: value})
    return [ x for x in cursor ]


def get_items(id_list):
    # TODO: better way to do this than multiple queries?
    items = []
    for the_id in id_list:
        doc = thing_c.find_one({'id': the_id})
        if doc:
            items.append(doc)
    return items


def insert(item):
    item["dateCreated"] = time.time()
    if not "children" in item:
        item["children"] = []
    validictory.validate(item, schema)
    thing_c.insert(item)
