# #import JSON

# # import json

# # with open('produk.json') as data:
# #     output = json.load(data)

# # print(output)
# # print(output[len(output)-1])
# # print(output[0::2])

import csv
import json

# with open('data2.txt') as dataku:
#     output = csv.reader(dataku)
#     hasil = []
#     hasil2 = []
#     for x in output:
#         hasil2.append(x)
#     for y in range(1, len(hasil2)-1):
#         data = {
#             'no': hasil2[y][0],
#             'nama': hasil2[y][1],
#             'kota': hasil2[y][2]
#         }
#         hasil.append(data)

# print(hasil)


# #ke Json

# hasilJson = json.dumps(hasil)
# file = open('csv.json', 'w')

# file.write(hasilJson)
# file.close()

##############

import csv
import json

# with open ('data2.csv', 'r') as dataku:
#     output = csv.DictReader(dataku)
#     for x in output:
#         print(dict(x))


# with open ('data2.csv', 'r') as dataku:
#     output = csv.DictReader(dataku)
#     hasil = []
#     for x in output:
#         hasil.append(dict(x))
# print(hasil)

# csv.register_dialect(
#     'pisahkomaspasi',
#     delimiter = ',',
#     skipinitialspace = True
# )

# csv.register_dialect(
#     'pisahkomaspasi',
#     delimiter = '|',
#     skipinitialspace = True
# )

# with open ('data1.csv', 'r') as dataku:
#     output = csv.reader(dataku, delimiter = '|')
#     for x in output:
#         print(x)

# listku = [
#     ['no', 'produk', 'harga'],
#     ['1','Batik', 250000],
#     ['2','Celana', 300000],
#     ['3','Drone', 1000000],
#     ['4','Kamera', 2000000],
#     ['5','Balon Udata', 2500000],
# ]

# apabila mau pake tititkoma
# csv.register_dialect(
#     'pisahtitikoma',
#     delimiter =';'
# )



# with open('gudang.csv', 'w', newline = '') as fileku:
#     tulis = csv.writer(fileku, dialect = 'pisahtitikoma')
#     tulis.writerows(listku)

# with open('gudang.csv', 'w') as fileku:
#     tulis = csv.writer(fileku)
#     for i in listku:
#         tulis.writerow(i)


# csv.register_dialect(
#     'pisahtitikoma', delimiter = ':'
# )

# csv.register_dialect(
#     'pisahtitik2',
#     delimiter =';'
# )

# with open('gudang.csv', 'w', newline = '') as fileku:
#     tulis = csv.writer(fileku, dialect= 'pisahtitik2')
#     tulis.writerows(listku)

# print(csv.list_dialects())

listku = [
  {'no': 1, 'nama': 'Andi'},
  {'no': 2, 'nama': 'Budi'},
  {'no': 3, 'nama': 'Caca'},
  {'no': 4, 'nama': 'Deni'},
  {'no': 5, 'nama': 'Euis'},
]

with open('staff.csv', 'w', newline='') as fileku:
    kolom = ['no', 'nama']
    tulis = csv.DictWriter(fileku, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(listku)


