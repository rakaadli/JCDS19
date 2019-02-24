# import numpy as np
# import csv

# with open('fifa.csv','r') as fifa19:
#     reader = csv.reader(fifa19)
#     for row in reader:
#         print(row)

# x ,y = np.loadtxt('0.csv',delimiter=',', unpack=True, skiprows =1)

# print(x)
# print(y)

# print(x.max())
# print(x.min())

# import matplotlib.pyplot as plt
# import numpy as np

# x = [1,2,3,4]
# x1 = [3,1,2,4]
# x2 = [1,2,3,4,5,6,7,8,9]
# x2 = np.array(x2)
# y = [2,4,6,8]
# y1 = [2,8,4,1]
# y2 = [1,4,9,3,5,8,4,2,5]
# plt.plot(x2,y2,y2,x2)
# plt.plot(x2,x2**3,'--', color = 'green',linewidth =5)
# plt.fill_between(x2,x2**3,205,facecolor='#800000',alpha=0.4)
# plt.fill_between(x2,x2[8],205,facecolor='#800000',alpha=0.4)
# plt.fill_between(x2,x2[2],x2[7],facecolor='#800000',alpha=0.4)
# plt.plot(x2,x2,'ro',x2,x2**2,'r--',x2,x2**3,'bs') #g^ r* y-- g-- b. ro -
# plt.plot(x2,y2, 'ro')
# plt.xlabel('Nilai X')
# plt.ylabel('Nilai Y')
# plt.grid(True, color='blue', linestyle='--',linewidth=5)
# # plt.legend(['Dataku'])
# plt.legend(['a x a', 'a x aa', 'a x aaa'])
# plt.title('Uji coba visualisasi data')
# plt.subplots_adjust(
#     left = 0.35, bottom = 0.20, right = 0.95,
#     top = 0.90, wspace = 0.2, hspace = 0.2
# )
# plt.show()

# 3x+2y=12

# |3 2| |x| = 12
# |0 0| |y| = 12

import numpy as np
import matplotlib.pyplot as plt

# a = np.array([[3]])
# b = np.array([[2]])
# c = np.array([12])

# x = np.linalg.solve(a,c) # x ketika y = 0 
# y = np.linalg.solve(b,c) # y ketika x = 0

# print(x,y)

# titikA = np.array([x[0],0])
# titikB = np.array([0,y[0]])

# titikC = np.array([0,1])
# titikD = np.array([-1,8])


# print(titikA)
# print(titikB)

# plt.plot(titikA,titikB,'r--',titikC,titikD,'g-')
# plt.show()

# x = np.arange(1,10,2)
# w = np.arange(0,3 * np.pi, 0.1)
# x = np.sin(w)
# y = np.cos(w)
# z = np.tan(w)
# print(x)

# plt.plot(w,x,'r--',w,y,'g-',w,z,'b-')
# plt.grid(True)
# plt.title('Grafik Sinus')
# plt.legend(['Sinus', 'cosinus','tangent'])
# plt.show()

w = ['A','B','C','D','E']
x = [2,4,6,8,10]
y = [2,6,3,8,10]
z = [1,3,5,7,9]

plt.bar(w,y,color='red')
plt.plot(w,y,'r--')
plt.fill_between(w,y,0, alpha=0.1)
plt.grid(True , color='cyan', linestyle='--')
plt.show()