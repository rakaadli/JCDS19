#guabikinjson ke a json
# import json

# file = open('a.json','w')

# data = [
#     {'nama':'raka'},
#     {'usia':24},
#     {'kota':'Jakarta'},
# ]

# dataJSON = json.dumps(data)
# file.write(dataJSON)
# file.close()

#insert mongo
# db.gudang.insert([
# {nama: 'kaos','harga':10000},
# {nama: 'jaket','harga':20000},
# {nama: 'celana', harga: 30000}])

#gua bikin json ke datascience_mongo
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["datascience"]
isicoll = mydb["gudang"]

# alldb = myclient.list_database_names()
# isidata = {}
# namabarang = input("masukan nama barang:")
# hargabarang = int(input("masukan harga barang:"))

# isidata['nama'] = namabarang
# isidata['harga'] = hargabarang

# newdata = isidata
# add = isicoll.insert_one(newdata)
# isiid = add.inserted_id
# for i in isicoll.find({'_id':isiid}):
#     print('Data Sukses Terkirim')
#     print(i)

################################################HAPUS
# data = {'nama':'sepatu'}
# isicoll.delete_one(data)

#########################################dari gudang monggodb ke json
# import json

# file = open('b.json','w')

# data= []


# for i in isicoll.find():
#     data2 ={
#         '_id' : str(i['_id']),
#         'nama' : i['nama'],
#         'harga': i['harga']
#     }
#     data.append(data2)

# dataJSON = json.dumps(data)
# file.write(dataJSON)
# file.close()

#########################################dari gudang monggodb ke CSV

import csv
import json

data= []


for i in isicoll.find():
    data2 ={
        '_id' : str(i['_id']),
        'nama' : i['nama'],
        'harga': i['harga']
    }
    data.append(data2)


dataCSV = json.dumps(data)
with open('c.csv','w',newline='') as c:
    createcsv = csv.DictWriter(c,fieldnames=['_id','nama','harga'])
    # file.write(dataCSV)
    createcsv.writeheader()
    createcsv.writerows(data)

##############mongo ke mysql