import pymongo
from config import DBNAME
from testdata import everything

c = pymongo.Connection('localhost')

db = c[DBNAME]
coll = db["everything"]

for t in everything:
    coll.insert(t)
