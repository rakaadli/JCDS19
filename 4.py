#function

# def halo():
#     print('Halo, ini function')

# halo()    
# halo()

#functiondengan parameter

# def luaspersegi():
#     Sisi = 12
#     print(Sisi ** 2)

# luaspersegi()

# def luaspersegi(Sisi):
    
#     print(Sisi ** 2)

# luaspersegi(12)
# luaspersegi(8)
# luaspersegi(10)

# #function dengan 2 parameter
# def luaspersegiPjg(pjg, lebar):
#     Luas = pjg*lebar
#     print('Luas Persegi Panjang dengan P=', pjg, '& L=', lebar, 'adalah L=', Luas)

# luaspersegiPjg(8,4)
# luaspersegiPjg(12,10)

# #function dengan 3 parameter
# def trapesium(AD, BC ,T):
#     LuasTrapesium = (AD+BC)*(T/2)
#     print(LuasTrapesium)
    

# trapesium(10,8,4)

#konveter dari IDR <=> USD

# def konverter(A,IDRUSD):
#     A = IDRUSD
#     IDRUSD = 0.00007*2
#     print(IDRUSD)

# konverter(2,'IDRUSD')

# def konverter(B,USDIDR):
#     B = USDIDR
#     USDIDR = 14000*2
#     print(USDIDR)

# konverter(2,'USDIDR')

# #dictionary data kurs
# datakurs = {
#     'USD-IDR' : 14000,
#     'IDR-USD' : 0.00007,
# }

# def konversi(nilai, metode):
#     if metode == 'USD-IDR':
#         kurs = datakurs['USD-IDR']
#         print('USD', nilai, 'setara = IDR', nilai*kurs)
#     elif metode == 'IDR-USD' :
#         kurs = datakurs[metode]
#         print('IDR', nilai, 'setara = USD', nilai*kurs)
#     else:
#         print('Mohon maaf, hanya melayani USD <=> IDR')

# konversi(2, 'USD-IDR')
# konversi(200000, 'IDR-USD')
# konversi(3,'USD-JPY')

# #dictionary data kurs
# datakurs = {
#     'USD-IDR' : 14000,
#     'IDR-USD' : 0.00007,
# }


# def konversi():
#     metode = input('Silakan masukkan metode konversi :')
#     nilai = float(input('Silakan masukan nominal : '))
#     if metode == 'USD-IDR':
#         kurs = datakurs['USD-IDR']
#         print('USD', nilai, 'setara = IDR', nilai*kurs)
#     elif metode == 'IDR-USD' :
#         kurs = datakurs[metode]
#         print('IDR', nilai, 'setara = USD', nilai*kurs)
#     else:
#         print('Mohon maaf, hanya melayani USD <=> IDR')

# konversi()

# return function
# def luas(x):
#     print(x *x)

# def luas2(y):
#     return y*y



# luas(12)
# # luas2(8) ga keluar
# print(luas2(8))

# def ganjilgenap(angka):
#     if angka % 2 == 0:
#         return'Angka ' + str(angka) + ' Tergolong GENAP'
#     else:
#         return 'Angka'+ str(angka) + ' Tergolong Ganjil'

# print(ganjilgenap(12))

# def fungsi():
#     angka = 2
#     hasil = angka + angka * angka
#     print(hasil)
#     print(angka)
#     print('Program selesai!')

# fungsi()

#looping

# while lops

# angka = 0
# while angka <= 6:
#     print(angka)
#     angka +=1

# password = '12345678'
# inputuser = ''
# angka = 1


# while inputuser != password:
#     inputuser = input('ketikkan password : ')
#     angka += 1
#     if inputuser != password and angka <= 5:
#         print('Password salah silahkan coba ke ' + str(angka))
#     elif inputuser != password and angka>= 5:
#          print('gagal maning')
#     else:
        
#         print('Password benar!')


# while True:
#     inputuser = input('Ketikan nama anda:')
#     print('Halo', inputuser)

# password = '12345678'
# inputuser = ''
# angka = 1
# tebakanke = 0
# batastebakan = 5
# melebihibatas = False

# while inputuser != password and not melebihibatas :
#     if tebakanke <= batastebakan:
#         inputuser = input('ketikkan password : ')
#         if inputuser != password and tebakanke < 5:
#             tebakanke +=1
#             print('Password salah silahkan coba ke ' + str(tebakanke))
#         elif inputuser != password and tebakanke == 5:
#             tebakanke +=1
#             print('Password Salah! kesempatan habis!')
#         else:
#             print('Selamat password anda benar')
#     else:
#         melebihibatas=True
#         print('Mohon maaf, coba lain kali')   

# for loop

# nama = 'Purwadhika'
# nama = ['Andi', 'Budi', 'Caca']

# for data in nama:
#     print(data, 'Susato')

# for elemen in range(6):
#     print(elemen)

# for data in nama:
#     print(data, 'Susanto')

# for data in range(len(nama)):
#     print(nama[data])

for x in [1,2,3,4,5]:
    print(x)

for i in range(5):
    print(i, 'susanto')

    