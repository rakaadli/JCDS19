import numpy as np

# a = ['Andi','Budi', 'Caca']
# b = np.array(a)


# # print(a)
# # print(b)
# print(a[0] + ' Susilo')
# print(b[0] + ' Susilo')


# a = ['Andi','Budi', 'Caca']
# b = [1,2,3]
# z= ['@','#','!']
# c = np.array([a,b, z])

# print(c[0])
# print(c[1])
# print(c[0][1])
# print(c[0,1])
# print(c.ndim)

satu = np.array(['andi','Budi', 'Caca'])
dua = np.array([['andi','Budi', 'Caca']])
tiga = np.array([[['andi', 'budi', 'caca']]])

a =  np.array([[[[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]]]])

b =  np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

# print(satu.ndim)
# print(dua.ndim)
# print(tiga.ndim)

# print(a.ndim)
# print(a[0,0,0,0,0])
# print(a.size) #jumlah elemen
# print(a.itemsize) #jumlah elemen tiap array dalam satuan byte

# print(satu.shape)
# print(dua.shape)

# dua = dua.reshape(3,1)
# print(dua)
# print(dua.shape)

# print(dua[0,2])
# print(dua[0][2])
# print(b[0,2])
# print(b[0][2])
# print(b[0:2], [0,2])

# print(b[0:4])
# print(b.ndim)
# print(b.max())
# print(b.min())
# print(b.sum(axis=0))
# print(b.sum(axis=1))
# print(np.sqrt(b))

# a = np.linspace(1,10,19)

# print(a)

# print(np.arange(10))
# print(np.arange(1,10))
# print(np.arange(1,10,2))

x=np.sin(0)
y=np.cos(0)
z=np.tan(0)

print(x)
print(y)
print(z)

print(np.log([1,2,3])) #ln e = 2,78
print(np.log10([100,10000])) #log10

print(np.exp([1,2,3]))

# e = euler = 2.718
# e ** x