import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import axes3d

# x = np.arange(10)
# y = np.arange(0,20,2)
# z = np.arange(1,21,2)
# z1 = np.arange(21,1,-2)

# plt.style.use('fast')
# style.use('fivethirtyeight')
#untuk tau ada style apa aja
# print(plt.style.available)

# plot, plot dan bar
# plt.plot(x,y,'r-')
# plt.plot(x,y,'go')
# plt.bar(x,y, color='black',yerr=0.5,bottom=z1)
# plt.plot(x,z1,'b-')
# plt.plot(x,z1,'yo')
# plt.bar(x,z1, color='yellow', yerr=.5)

# plt.text(5,21,'halo!')
# plt.grid(True)
# plt.xticks(x)


#Scatter
# plt.scatter(x,y,color='k',marker='*', s=300)
# plt.plot(x,z1)

# slice= [8,3,8,4]
# aktivitas = ['Tidur','Makan','Belerja','Olahraga']
# # plt.pie(slice,labels=aktivitas)

# x=[0,1,2,3]

# plt.pie(slice,
#     labels = aktivitas,
#     colors = ['c','m','y','k'],
#     startangle = 90,
#     shadow = True,
#     explode = (0,.2,0,.4)
# )

#visualisasi
# plt.bar(x,y, color='blue',yerr=0.5)

# for i in x:
#     plt.text(i - .1,y[i]+1,y[i])

# plt.annotate(
#     'Ini Tertinggi',
#     xy = (9,18),
#     xytext=(5,21),
#     # arrowprops = dict(facecolor='red',shrink=0.1),
#     arrowprops = dict(arrowstyle = 'wedge')

# )




# plt.show()


#4.py figure

# x1 = np.arange(10)

# plt.figure('Halo 1',figsize=(9,3))
# plt.subplot(1,3,1)
# plt.bar(x1,x1)
# plt.subplot(1,3,2)
# plt.plot(x1,x1**2)
# plt.subplot(1,3,3)
# plt.scatter(x1,x1**3)
# plt.suptitle('Tes bikin 3 plot 1 figure')
# # plt.figure('Halo 2')

#4figure
# plt.figure('Halo 1',figsize=(8,2))
# plt.subplot(1,4,1)
# plt.bar(x1,x1)
# plt.subplot(1,4,2)
# plt.plot(x1,x1**2)
# plt.subplot(1,4,3)
# plt.scatter(x1,x1**3)
# plt.subplot(1,4,4)
# plt.pie([4,4,4,4],labels=['A','B','C','D'])
# plt.suptitle('Tes bikin 4 plot 1 figure')
# plt.figure('Halo 2')

# plt.figure('Halo 1',figsize=(8,8))
# plt.subplot(2,2,1)
# plt.bar(x1,x1)
# plt.subplot(2,2,2)
# plt.plot(x1,x1**2)
# plt.subplot(2,2,3)
# plt.scatter(x1,x1**3)
# plt.subplot(2,2,4)
# plt.pie([4,4,4,4],labels=['A','B','C','D'])
# plt.suptitle('Tes bikin 4 plot figure atas bawah')

# plt.show()

# Insert Image: PNG
# gambar = mpimg.imread('110F.png')
# xgbr = gambar[:,:,0]
# x2 = np.arange(350)

# plt.imshow(xgbr, cmap='hot')
# plt.plot(x2,x2)

# plt.show()

plt.figure('3D plotting')
i = plt.subplot(111, projection='3d')

x= np.arange(10)
y= np.arange(10)
z= np.array([(x)])
xn = np.arange(10,0,-1)
yn = np.arange(10,0,-1)
zn = np.array([xn])

i.plot_wireframe(x,y,z)
i.plot_wireframe(x,yn,zn)
i.scatter(x,y,z, color='red',marker='*',s=200)

xalas = np.arange(10)
yalas = np.arange(10)
zalas = np.zeros(10)
xdinding = np.ones(10)
ydinding = np.ones(10)
zdinding = np.arange(10)

i.bar3d(xalas,yalas,zalas,xdinding,ydinding,zdinding)
i.set_xlabel('ini X')
i.set_ylabel('ini Y')
i.set_zlabel('ini Z')
plt.show()