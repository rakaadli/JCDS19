
# file handiling
# 'r'ead. 'w'rite, 'a'ppend, 'r+' read & write, 'x' create

# file = open('data1.txt', 'r')
# print(file.read()) #check if it can be read
# print(file.readable()) #read all files
# print(file.readline()) #hanya 1 baris
# print(file.readlines()) #Menampilkan list

# file = open('data1.txt', 'w')
# file.write('Euis')
# file.write('\nFafa')

# file = open('data1.txt', 'a')
# file.write('/nGilang')

# file = open('data1.txt', 'x') # nambah

# punya raka
# file = open('data2.txt', 'x') 
# file = open('data2.txt', 'a')
# file.write('Andi')
# file.write('\nBudi')
# file.write('\nCaca')

#punya mas lintang
list = ['Andi', 'Budi', 'Caca']

# data = open('data2.txt', 'a')

# for nama in list:
#     data.write(nama + '\n')

# data = open('tes.py', 'x')

# data.write('Halo')
# data.write('print(\'Halo\')')

# import os
# os.remove('tes.py')
# os.rmdir('ok') #folder yg kosong aja yg bisa

# file = open('data1.json', 'a')

# # file.write('[{"nama": "Doffy"}, {"nama": "non"}, {"nama": "nin"}]')
# list = [
#     {'nama':'andi'},
#     {'nama':'andre'},
#     {'nama':'ando'}
# ]

import json

# #json ke dictionary
# dataDict = {'nama':'Andi'}
# dataJson = json.dumps(dataDict)

# print(dataJson)

#dictionary to Json
# dataJson = '{"nama":"Andi"}'
# dataDict = json.loads(dataJson)

# print(dataDict)
# print(dataDict['nama'])

# #list 
# dataDict = {'nama':'Andi'}
# dataList = [{'nama':'Andi'},{'nama':'Andi'}]
# dataJson = json.dumps(dataList)

# print(dataJson)

# file = open('data.json', 'r')
# dataJson = file.read()
# print(dataJson)
# print(type(dataJson))

# print(file.read())

# dataPy = json.loads(dataJson)
# print(dataPy)
# print(type(dataPy))

import requests

# nama = input('Ketik nama pemain:')
# url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p='+nama

# data = requests.get(url)
# output = data.json()
# # print(output)
# print(output['player'][0]['strNationality'])

nama = input('Ketik klub bola:')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+nama

data = requests.get(url)
output = data.json()
# print(output)
listpemain = data.json()['player']
# print(output['player'][0]['strNationality'])
# print(listpemain)

# for name in listpemain:
#     print(name['strPlayer'])

for name in listpemain:
    if name['strPosition'] == 'Goalkeeper':
        print(name['strPlayer'])
    else:
        pass

