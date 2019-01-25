# list = [

#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(list)
# print((list[0]))
# print(list[2][0])

# tuple = (

#     (1,2,3),
#     (4,5,6),
#     (7,8,9)
# )

# print(tuple)

# tuple( gagal
#     (
#         ('a','b','c'),
#         ('d','e','f'),
#         ('g','h','i')
#     ),
#     (4,5,6),
#     (7,8,9)
#     )

# print(tuple[0][1][2])

# angka = [
# (1,2,3),
# (4,5,6),
# (7,8,9)
# ]

# nomor= (
# [1,2,3],
# [4,5,6],
# [7,8,9]

# )
# print(angka[1][1])
# angka[2] = 'Andi'
# print(angka)
# nomor[0][0]='Andi'
# print(nomor)

# tes={1,2,3}

# print(tes)

# for elemen in tes:
#     print(elemen)



#check element
# print(2 in tes)

#add an element
# tes.add('Budi')
# print(tes)

#add elements
# tes.update(['3','4','Caca','Deni'])
# print(tes)

#remove elements = remove()
# tes.remove('Budi')
# print(tes)

#remove elements = .discard()
# tes.discard('Bambang')
# print(tes)

#delete all elements
# tes.clear()
# print(tes)

# #set
# del tes
# print(tes)

#Dictionary = { key : value }

# bulan= {
#     1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni', 7:'Juli', 8:'Agustus',9:'September',10:'Oktober',11:'November',12:'Desember'
# }

# print(bulan[1])
#print(bulan.get(2))
# print(bulan.get(13, 'Maaf data tidak tersedia.'))

#change value
# bulan[2]='February'
# print(bulan[2])

#add item
# bulan[13]='xpander'
# # val = ['haha','hihi'] ga bisa
# # bulan[list] = val
# print(bulan)

#update
# bulan.update({13: 'Xpanda'})
# print(bulan)

#Remove item
# bulan.pop(13)
# print(bulan)

# del bulan[2]
# print(bulan)

# student = ['Andi','Budi','Caca']

# isilah = input('Ketikan nama anda:')
# student.append(isilah)
# print(str(student))

#ifstatement

# if condition: 
#     program()

# elif condition:
#     program()

# berkerja = True
# tahun = 3

# if berkerja and tahun >=2 : 
#     # if berkerja == True
#     # print('Anda sudah bekerja selama', tahun, 'tahun.')
#     # print('Anda sudah bekerja selama '+ str(tahun) + ' tahun.')
#     print('Anda berpengalaman')
# elif berkerja and tahun < 2 :
#     # print('Anda belum bekerja')
#     print('Anda pegawai baru')
# elif not berkerja and tahun <2 :
#     print('anda sedang mencari kerja')
# else :
#     print ('anda sudah lama tidak bekerja')

# x = 12
# y ='12'
# z=13

# print(x==int(y))
# if x == y or x<z:
#     print('nilai X tidak sama dengan y atau < z')
# else:
#     print('Kondisi tidak terpenuhi')

# angka=11000549439
# genap = 0
# genap =+ 2
# ganjil = 1
# ganjil =+ 2

# if angka == genap:
#     print('angka' + str(angka) + ' Tergolong genap')
# else:
#     print('angka' + str(angka) + ' Tergolong ganjil')

# angka = 10092

# if angka % 2 == 0:
#     print('Angka' , angka , ' Tergolong GENAP!')
# else:
#     print('Angka', angka, 'Tergolong GANJIL!' )

# angka1 = float(input('masukan angka 1 : ' ))
# operator = input('Masukan Operator : (+ - * /) ')
# angka2 = float(input('Masukan angka 2 : '))

# if operator == '+':
#     print('angka1 + angka2')
# elif operator == '-':
#     print(angka1-angka2)
# elif operator == '/':
#     print(angka1/angka2)
# elif operator == '*':
#     print(angka1*angka2)
# else:
#     print('operator salah')

massa = int(input('Masukan Massa dalam kg:'))
Tinggi = int(input('Masukan tinggi dalam cm:'))
Tinggi = Tinggi*0.01
IMT = massa/Tinggi**2
if IMT <= 18.5 :
    print('massa'+ str(massa) +'& Tinggi' + str(Tinggi) + 'IMT =' + str(IMT) + 'Berat Badan Kurang')
elif IMT >= 18.5 and IMT <24.9 :
    print('massa'+ str(massa) +'& Tinggi' + str(Tinggi) + 'IMT =' + str(IMT) + 'Berat Badan Ideal')
elif IMT >= 24.9 and IMT <29.9 :
    print('massa'+ str(massa) +'& Tinggi' + str(Tinggi) + 'IMT =' + str(IMT) + 'Berat Berlebih')
elif IMT >= 29.9 and IMT <39.9 :
    print('massa'+ str(massa) +'& Tinggi' + str(Tinggi) + 'IMT =' + str(IMT) + 'Berat Badan Ideal')
else:
    print('Ada yang salah broo' + str(IMT))

