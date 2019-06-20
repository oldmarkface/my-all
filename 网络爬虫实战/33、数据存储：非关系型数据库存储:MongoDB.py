import pymongo
client = pymongo.MongoClient(host='localhost',port=27017)
student={
    'name':'mark'
}
collection=client.test.colleaction

# result=collection.insert(student)
# print(result)

result=collection.insert_one(student)
print(result.inserted_id)