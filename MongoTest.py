import pymongo
client = pymongo.MongoClient("mongodb+srv://kshamaPathak:data_science@1@cluster0.lytd63w.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)