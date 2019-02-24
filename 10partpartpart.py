import json
# file = open('a.json', 'w')
# data=[
#     {'nama': 'Andi'},
#     {'nama': 'Budi'},
#     {'nama': 'Caca'}
# ]
# dataJson = json.dumps(data)

# file.write(dataJson)
# file.close()


import pymongo

url= 'monggodb://localhost:27017'
mydb = pymongo.MongoClient()

newdb = mydb["gudang"]
newcol = newdb["produk"]
data =  []

for i in newcol.find():
    # print(i["_id"])
    # data.append(i)
    d = {
        '_id' : str(i['_id']),
        'nama' : i['nama'],
        'harga' : i['harga'],
        # 'Kota' : i['Kota'],
        # 'kota' : i['kota']
    }
    data.append(d)
print(data)

file = open('produk.json', 'w')
dataJson = json.dumps(data)

file.write(dataJson)
file.close()

# ctrl shift p