import pymongo

url= 'monggodb://localhost:27017'
mydb = pymongo.MongoClient()

nama = input('ketik nama produk: ')
harga = input('Ketik harga produk: ')

newdb = mydb["gudang"]
newcol = newdb["produk"]
newdata = {"nama" : nama, "harga" : int(harga)}
# newdata = {"nama" : "baju", "harga" : 700000}
add = newcol.insert_one(newdata)
newid = add.inserted_id

for data in newcol.find({'_id': newid}):
    print('Data Sukses Terkirim')
    print(data)

