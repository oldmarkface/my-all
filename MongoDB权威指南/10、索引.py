import json

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database

def insert_some():
    for i in range(10000000):
        db.users.insert_one({
            'i':i,
            'name':'mark'
        })

def find_explain():
    explain=db.users.find({'i':9999999}).explain()
    print(json.dumps(explain,indent=4))
def ensure_index():
    result=db.users.create_index('i')
    print(result)
if __name__ == '__main__':
    #db.users.drop()
    #insert_some()
    #ensure_index()
    find_explain()
