import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as ani
import csv


# plt.figure('3D plotting')
# i = plt.subplot(111, projection='3d')

# xalas = np.arange(10)
# yalas = np.ones(10)
# xalas2 = np.arange(10,0,-1)
# # yalas2 = np.arange(10,0,-1)
# yalas2 = np.repeat(3,10)
# zalas = np.zeros(10)
# xdinding = np.repeat(0.5,10)
# ydinding = np.repeat(0.5,10)
# zdinding = np.arange(10)

# i.bar3d(
#     xalas,yalas,zalas,
#     xdinding,ydinding,zdinding,
#     color = 'yellow'
# )

# i.bar3d(
#     xalas2,yalas2,zalas,
#     xdinding,ydinding,zdinding,
#     color = 'green'
# )

# i.set_ylim(0.10)
# i.set_xlim(0.10)
# i.set_xlabel('Ini X')
# i.set_ylabel('Ini Y')
# i.set_zlabel('Ini Z')

# i.text(5,5,4, 'Halo!',color='red')
# i.text2D(1,1,'Halo!', color='red',transform = i.transAxes)

# # legendAbu = plt.Rectangle((0,0),1,1,fc='grey')
# # legendkuning = plt.Rectangle((0,0), 1,1,fc='yellow')
# # i.legend([legendAbu, legendkuning], ['a','b'])


# legendAbu = plt.Rectangle((1,3),1,3,fc='grey')
# legendkuning = plt.Rectangle((1,3), 1,3,fc='yellow')
# i.legend([legendAbu, legendkuning], ['a','b'])

# plt.show()

#######################################################################################

# x = np.arange(1,11,1)
# y = np.array([1,4,9,3,5,8,4,10,9,6])


# i = plt.subplot2grid((1,1),(0,0))
# i.plot(x,y)
# i.bar(x,y)

# i.spines['left'].set_color('r')
# i.spines['left'].set_linewidth(5)
# i.spines['bottom'].set_visible(False)

# i.tick_params(axis='both', color='red', colors='yellow', labelsize ='large')

# i.axhline(5, color='g',linewidth=3)
# i.axvline(5, color='g',linewidth=3)
# plt.axhline(3)
# i.fill_between(x,5,3,facecolor='g',alpha=0.2)


# plt.show()

################################################################################

# fig = plt.figure('Tes Animasi')
# i = fig.add_subplot(1,1,1)

# def grafik(s):
#     x = []
#     y = []
#     data = open('5.csv','r').read()
#     baris = data.split('\n')
#     for n in baris:
#         a, b = n.split(',')
#         x.append(a)
#         y.append(b)    
#     i.clear()
#     i.plot(x,y)

# run = ani.FuncAnimation(fig,grafik,interval=1000)
# plt.show()

##################################################################################

alldata=[]
prov = []
rokok15 = []
rokok16 = []

with open('rokok.csv','r') as fileku:
    reader = csv.reader(fileku)
    for x in reader:
        # prov.append(x[0])
        # rokok15.append(float(x[1]))
        # rokok16.append(float(x[2]))
        data = [x[0], float(x[1]), float(x[2])]
        alldata.append(data)
        prov.append(x[0])
        rokok15.append(float(x[1]))
        rokok16.append(float(x[2]))

alldata.remove(alldata[0])
prov.remove(prov[0])
rokok15.remove(rokok15[0])
rokok16.remove(rokok16[0])

ratarokok15 = np.mean(rokok15)
ratarokok16 = np.mean(rokok16)

overrokok = []
provover = []
rokok15over = []
rokok16over = []
for x in alldata:
    if x[1] >  ratarokok15 and x[2] > ratarokok16:
        overrokok.append(x)
        provover.append(x[0])
        rokok15over.append(x[1])
        rokok16over.append(x[2])

# plt.bar(provover,rokok15over)
# plt.bar(provover,rokok16over)
# plt.plot(provover,np.repeat(ratarokok15,len(provover)), 'g-', linewidth=3)
# plt.plot(provover,np.repeat(ratarokok16,len(provover)), 'g-', linewidth=3)
# plt.ylim(25,35)
# plt.xticks(rotation=90)
# plt.legend(['2015','2016'])
# plt.show()

plt.figure('3D plotting')
i = plt.subplot(111, projection='3d')
#titik mulai alas
xalas = np.arange(len(provover))
yalas = np.ones(len(provover))
zalas = np.zeros(len(provover))
xalas2 = np.arange(len(provover))
yalas2 = np.repeat(4,len(provover))

xdinding = np.repeat(0.5,len(provover)) #buat lebar
ydinding = np.repeat(0.5,len(provover)) # buat panjang
zdinding1 = rokok15over
zdinding2 = rokok16over

i.bar3d(
    xalas,yalas,zalas,
    xdinding,ydinding,zdinding1,
    color = 'yellow'
)

i.bar3d(
    xalas,yalas2,zalas,
    xdinding,ydinding,zdinding2,
    color = 'green'
)

i.set_ylim(0,len(provover))
i.set_xlim(0,len(provover))
i.set_xlabel('Ini X')
i.set_ylabel('Ini Y')
i.set_zlabel('Ini Z')

plt.xticks(xalas,provover,rotation=90)

# i.text(5,5,4, 'Halo!',color='red')
# i.text2D(1,1,'Halo!', color='red',transform = i.transAxes)

legendAbu = plt.Rectangle((0,0),1,1,fc='yellow')
legendkuning = plt.Rectangle((0,0), 1,1,fc='green')
i.legend([legendAbu, legendkuning], ['rokok 15','rokok 16'])


# legendAbu = plt.Rectangle((1,3),1,3,fc='grey')
# legendkuning = plt.Rectangle((1,3), 1,3,fc='yellow')
# i.legend([legendAbu, legendkuning], ['a','b'])

plt.show()