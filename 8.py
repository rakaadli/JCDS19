#quotes design
#wp-json posts

# import json
import requests
# import requests

# url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'

# data = requests.get(url)
# listQuote = data.json()

# print(listQuote)
# print(listQuote[0]['content'])

# kode = input('ketikan nama bank:').lower()
# url = 'https://kurs.web.id/api/v1/' + kode

# data = requests.get(url)
# Datakursbank = data.json()


# if Datakursbank['error'] == "true":

#     print('maaf data bank tidak tersedia')

# else:
#     pass
#     jualbeli1 = input('Kurs yang kamu punya? (IDR/USD/BTC)')
#     totaltukar = int(input('mau di tuker berapa?'))
#     kursbeli = int(Datakursbank['beli'])
#     kursjual = int(Datakursbank['jual'])
#     if jualbeli1 == 'IDR':
#         print(totaltukar/kursbeli + 'USD')
#     elif jualbeli1 == 'BTC':
#         print()
#     else:
#         print(totaltukar*kursjual+ 'IDR')

# print(Datakursbank['jual'])
# print(Datakursbank['beli'])



# kode = input('ketikan nama bank:').lower()
# url = 'https://kurs.web.id/api/v1/' + kode

# data = requests.get(url)
# Datakursbank = data.json()

# url ='https://blockchain.info/tobtc?currency=USD&value=1'

# dataBTC = requests.get(url)
# dollarBTC = dataBTC.json()

# if Datakursbank['error'] == "true":

#     print('maaf data bank tidak tersedia')

# else:
#     pass
#     jualbeli1 = input('Kurs yang mau diubah dari mana-kemana? (IDR/USD/BTC)')
#     totaltukar = int(input('mau di tuker berapa?'))
#     kursbeli = int(Datakursbank['beli'])
#     kursjual = int(Datakursbank['jual'])
#     totalbeliUSD = totaltukar/kursbeli
#     TotaljualIDR = totaltukar*kursjual
#     # adollarBTC = int(dollarBTC)
#     DolartoBTC = dollarBTC* int(totalbeliUSD)
#     if jualbeli1 == 'IDR':
#         print( str(totalbeliUSD) + 'USD')
#         mauBTC = input('want to change to bitcoin? (yes/no)')
#         if mauBTC == 'yes':
#             print(DolartoBTC * totalbeliUSD)
#         else:
#             print('total diterima : ' + DolartoBTC + 'BTC')
#     else:
#         print( str(TotaljualIDR) + 'IDR')
#         mauBTC = input('want to change to bitcoin? (yes/no)')
#         if mauBTC == 'yes':
#             print(DolartoBTC * TotaljualIDR)
#         else:
#             print('total diterima : ' + str(TotaljualIDR) + 'USD')

# appid = 'e48a7eddac52ba45d036c66ae136f14c'
# url = 'http://api.openweathermap.org/data/2.5/weather?q='
# cari = 'Jakarta' 

# data = requests.get(url+cari+'&APPID=' +appid)

# print(data.json()['weather'][0]['main'])

#punya si alvin
import requests

bank = input('Masukkan kode bank yang akan menjadi acuan : ').lower()
url = 'https://kurs.web.id/api/v1/' + bank
data = requests.get(url)
data = data.json()

print('Selamat datang')
print('Silahkan pilih konversi yang akan Anda lakukan :')
print(' (1) IDR indonesia => USD United States')
print(' (2) USD United States => IDR Indonesia')
print(' (3) IDR indonesia => Bitcoin')
print(' (4) USD United States => Bitcoin')

pil = input('Pilihan Anda (1/2/3/4) : ')

if pil == '1':
    uang = int(input('Masukkan jumlah Rupiah : Rp. '))
    hasil = uang / int(data['jual'])
    print(f"Rp.{uang} sama dengan US$.{hasil}")
elif pil == '2':
    uang = int(input('Masukkan jumlah Dollar : US$. '))
    hasil = uang * int(data['jual'])
    print(f"US$.{uang} sama dengan Rp.{hasil}")
elif pil == '3':
    uang = int(input('Masukkan jumlah Rupiah : Rp. '))
    uang2 = str(uang / int(data['jual']))
    hasil = requests.get(
        'https://blockchain.info/tobtc?currency=USD&value=' + uang2)
    print(f"Hasil konversi Rp. {uang} adalah BTC {hasil.json()}")
elif pil == '4':
    uang = input('Masukkan jumlah Dollar : US$. ')
    hasil = requests.get(
        'https://blockchain.info/tobtc?currency=USD&value=' + uang)
    print(f"Hasil konversi US$. {uang} adalah BTC {hasil.json()}")
else:
    print('YANG BENER AJA LAH, PILIHAN CUMA 1 - 4')

# print('%.4f' % (1324343032.324325235))
