import pymongo
client = pymongo.MongoClient("mongodb+srv://kshamaPathak:datascience1@cluster0.lytd63w.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
'''client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)'''
d={
    "name":"Kshama",
    "email":"kshamakulk@gmail.com",
    "surname":"Pathak"
}
db2=client['mongotest']
coll=db2['test']
coll.insert_one(d)