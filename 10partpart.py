import pymongo

url= 'monggodb://localhost:27017'
mydb = pymongo.MongoClient()

newdb = mydb["gudang"]
newcol = newdb["produk"]

data = {"nama" : "Drone"}
data = {}
# newcol.delete_one(data)
newcol.delete_many(data)

for x in newcol.find(data):
    print(x)

