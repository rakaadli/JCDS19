# x = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 3
# }



# print(x['a'])
# print(list(x.keys())[0])

# print(list(x.values()).index(2))

#key berdasarkan value
# print(list(x.keys())[list(x.values()).index(3)])


morse = {
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
#         hasil+= morse[i] + '/'
#  print(hasil)


# def ubahdarimorse(teks):
#     kalimat = teks.split(' / ')
#     # print(kalimat)
#     hasil = ''
#     for i in kalimat:
#         hasil += list(morse.keys())[list(morse.values()).index(i)]
#     print(hasil)

# ubahkemorse('Raka')
# ubahdarimorse('.... / .- / .-.. / ---')
    
# satuinput = input('Ketik karakter yang akan diubah =')
#     if satuinput == tekss:
#         ubahdarimorse(tekss)



# def ubah(tekss):
#     # print(tekss.isalpha())
#     if tekss.upper() == tekss.lower():
#         kalimat = tekss.split(' / ')
#         hasil = ''
#         for i in kalimat:
#             hasil += list(morse.keys())[list(morse.values()).index(i)]
#         print(hasil)
#     else :
#         kalimat = tekss.lower().replace(' ', '')
#         hasil = ''
#         for i in kalimat:
#                 hasil+= morse[i] + '/'
#         print(hasil)


# ubah(input('\n ketik karakter yang akan diubah : '))

#package = built-in & 3rd party
#package datetime

# import  datetime

# x = datetime.datetime.now()

# # print(x)
# waktu = str(x).split(' ')
# dateform = waktu[0]
# tahun = dateform.split('-')[0]
# bulan = dateform.split('-')[1]
# tanggal = dateform.split('-')[2]
# print(tanggal,bulan,tahun)
# hourForm = waktu[1]
# jam = hourForm.split(':')[0]
# menit = hourForm.split(':')[1]
# detik = hourForm.split(':')[2]
# print(jam, menit, detik)

# x = datetime.datetime.now()

# print(x.strftime('%A, %d - %m %B - %Y'))

# hari = {
#     'Monday' : 'Senin',
#     'Tuesday' : 'Selasa',
#     'Wednesday' : 'Rabu',
#     'Thursday' : 'Kamis',
#     'Friday' : 'Jum\'at',
#     'Saturday' : 'Sabtu'
# }

# print(hari[x.strftime('%A')])

# bulan = {
#     'January' : 'Januari',
#     'February' : 'Februari',
#     'Maret' : 'April',
#     'May' : 'Mei',
#     'June' : 'Juni',
#     'July' : 'Juli',
#     'August' : 'Agustus',
#     'September' : 'September',
#     'October' : 'Oktober',
#     'November' :'November',
#     'December' : 'Desember'  
# }

# print(bulan[x.strftime('%B')])

# print(x.strftime('%H')) #24 jam
# print(x.strftime('%I')) #12 jam
# print(x.strftime('%p'))
# print(x.strftime('%M'))
# print(x.strftime('%S'))

# import threading

# def printtiapdetik():
#     threading.Timer(1.0, printtiapdetik).start()
#     print('Halo Dunia!')

# printtiapdetik()

# import time
# import datetime



# def tes():
#     while True: 
#         print('Tes 1 2 3')
#         time.sleep(1)

# tes()


# def tes():
#     while True: 
#         x = datetime.datetime.now()
#         print(x.strftime('Sekarang jam %H:%M:%S WIB'))
#         time.sleep(1)

# tes()

# import test1

# print(test1.nama)
# print(test1.Usia)
# print(test1.Jomblo)
# print(test1.job[2])

# # print(test1.halo()) #None
# test1.halo('Ali')

# print(test1.kuadrat(8))

# import morse

# morse.ubah(input('\n ketik karakter yang akan diubah : '))

#lambda 

# def namafunction(param)
#     print(param)

# namafunction('Halo gaes!')

# cetak = lambda a : a
# print(cetak('halo'))

# def cetak2(a):
#     return a
# print(cetak2('haha'))


# cetak = lambda a : a + 2
# print(cetak(2))


# cetak = lambda a, b : a + b
# print(cetak(2,3))

# def tes(x):
#     return lambda a : a * x

# duakali = tes(2)
# tigakali = tes(3)
# empatkali  = tes(4)

# print(duakali(4))

#try except

try: 
    nilai = int(input('Ketik angka 1:'))
    nilai2 = int(input('Ketik angka 2 : '))
    print(nilai/nilai2)
    # print(int(nilai))
except ValueError:
    print('HAHA BEGO')
except ZeroDivisionError:
    print('ndak bisa di bagi 0 WOI!')