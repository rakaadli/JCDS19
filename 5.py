# for i in range(2,7):
#      print(i)
    
# star= ''
# for i in range(5):
#     star+= ' * '
#     print(star)

#https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/

# for i in range(5):
#     for j in range(6,10):
#         print(i,'&',j)

# i = 0 -j = 6 = 0&6
# i = 0 -j = 6 = 0&7
# i = 0 -j = 9 = 0&9 
# i = 0 -j = 10 xxxxx failed
# i - 1 -j = 6

list = [
    [1,2,3], 
    [4,5,6],
    [7,8,9]
]

# for baris in list:
#     print(baris)
#     for kolom in baris:
#         print(kolom)

# for baris in list:
#     print(baris[0])
#     print(baris[1])
#     print(baris[2])


# list = [
#    [
#     [1,2,3], 
#     [4,5,6],
#     [7,8,9]
#    ],
#    [
#     [10,11,12], 
#     [13,14,15],
#     [16,17,18]
#    ]
# ]

# for x in list:
#     for y in x:
#         for z in y:
#             print(z)

# list=[]
# i= 0
# while i<=1000:
#     list.append(i)
#     i += 1

# for data in list:
#     print(data)

# FizBuzz
# angka = 13
# function(13): 

# - kalo angka kelipatan 3 = 'dorr'
# - kalo angka kelipatan 5 = 'Cess'
# -kalo angka kelipatannya 3 dan 5 = 'Ting'


# list = []
# i = 0
# while i <= 15:
#     list.append(i)
#     i += 1

# for data in list:
#     if data % 5 == 0 and data % 3 == 0:
#         print('Dor')
#     elif data % 5 == 0:
#         print('Cess')
#     elif data % 3 == 0:
#         print('Ting')
#     else:
#         print(data)

# def FizBuzz(x):
#     for i in range(1, x+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('Ting')
#         elif i % 3 == 0:
#             print('Dor')
#         elif i % 5 == 0:
#             print('Cess')
#         else:
#             print(i)
# FizBuzz(50)

# def FizBuzz(x):
#     for i in range(1, x+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('Ting')
#         elif i % 3 == 0:
#             print('Dor')
#         elif i % 5 == 0:
#             print('Cess')
#         else:
#             print(i)
# FizBuzz(50)

import re
import sys

Morse = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e': '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm': '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-', 
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
    # . : '.-.-',
    # , : '--..--',
    # ? : '..--..',
    # / : '--..-.',
    # @ : '.--.-.',
    # 1 : '.----',
    # 2 : '..---',
    # 3 : '...--',
    # 4 : '....-',
    # 5 : '.....',
    # 6 : '-....',
    # 7 : '--...',
    # 8 : '---..',
    # 9 : '----.',
    # 0 : '-----',
}

# def ubahkemorse(teks):
#  kalimat = teks.lower().replace(' ', '')
#  hasil = ''
#  for i in kalimat:
#         hasil+= Morse[i] + '/'
#  print(hasil)

# ubahkemorse('Raka Adli Pramudita')

# KodeMorse = '.-/-...'

# def ubahkealfabet(KodeMorse):
#     isikodemorse = KodeMorse.replace(' ','')
#     alfabet=''
#     for kata in KodeMorse
#             alfabet += KodeMorse



# def decode(input):
#     hasil = ''
#     line = input.split('/')
#     for i in range(len(line)):
#         for key,value in Morse.items():
#             if line[i]==value:
#                 hasil+=key
#     print(hasil)
# decode('..-/.-.')

# def decode(input):
#     hasil = ''
#     line = input.split('/')
#     for i in range(len(line)):
#         for key,value in Morse.items():
#             if line[i]==value:
#                 hasil+=key
#     print(hasil)
# decode('..-/.-.')

'''
penerjemah dari morse
'''
mor={'.-':'a',
    '---.':'b',
    '-.-.':'c',
    '-..':'d',
    '.':'e',
    '..-.':'f',
    '--.':'g',
    '....':'h',
    '..':'i',
    '.---':'j',
    '-.-':'k',
    '.-..':'l',
    '--':'m',
    '-.':'n',
    '---':'o',
    '.--.':'p',
    '--.-':'q',
    '.-.':'r',
    '...':'s',
    '-':'t',
    '..-':'u',
    '...-':'v',
    '.--':'w',
    '-..-':'x',
    '-.--':'y',
    '--..':'z',
    ' ':' '}
def mors(b):
    #b=input('Masukkan morse, pisah dengan spasi setiap huruf dan / setiap kata: ')
    # a=b.replace('/', ' ')
    # c=a.split(' ')
    # print(c)
    # #li=len(a)
    # hasil=''
    # for i in c:
    #     hasil+=mor[i]
    # print(hasil)

    a=b.split('/')
    hasil=''
    print(a)
    # for i in range(len(a)):
    #     c=a[i].split(' ')
    #     print(c)
    #     for x in c:
    #             hasil+=mor[x]
    # print(hasil)

mors('-../../..-/../.-/.---/.-')