import pymongo

url= 'monggodb://localhost:27017'
mydb = pymongo.MongoClient()

newdb = mydb["gudang"]
newcol = newdb["produk"]
# newdata = {"nama" : "Drone", "harga" : 1200000}
# add = newcol.insert_one(newdata)

# alldb = mydb.list_database_names()
# print(alldb)
# print(add.inserted_id)


# for data in newcol.find():
#     print(data)

# for data in newcol.find({'nama': 'Drone'}):
#     print(data)

# for data in newcol.find({'harga': {'$lte': 1000000}}):
#     print(data)

#update data
# data = {"nama" : "Batik"}
# newdata = {"$set": {"nama": "Batik Jogja"}}
# newcol.update_one(data,newdata)

#update data banyak kota jakarta
# data = {}
# newdata = {"$set": {"kota": "Jakarta"}}
# newcol.update_many(data, newdata)

# for x in newcol.find({"nama": "Batik Jogja"}):
#     print(x)

data = {'$and':[{'harga': {'$gt': 300000}},{'harga': {'$lt': 1000000}}]}
newdata = {"$set": {"kota": "Bogor"}}
newcol.update_many(data, newdata)

for data in newcol.find():
    print(data)

