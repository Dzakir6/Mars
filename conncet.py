from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ns0bhrz.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'test': 'test1'
}
db.user01.insert_one(doc)