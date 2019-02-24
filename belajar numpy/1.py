import numpy as np

a = np.array([1,2,3,4,5])
a1 = np.array([[1,2,3],[4,5,6]])
b = [1,2,3,4,5]
c = 2

# print(2 * a)

# print(a1.size)

# print(a1.shape)
# print(a1 + a1)

# print(np.mean(a1))
# print(np.mean(b))

# print(np.median(a1))
# print(np.median(b))

# a2 = np.array([[2,12,8],[3,23,19]])

# print(np.mean(a2))

# | 2 12 8 | a1
# | 3 23 19 | a1
#  a0 a0 a0
# print(np.mean(a2,axis = 0))
# print(np.mean(a2,axis = 1))

# print(np.median(a2,axis = 0))
# print(np.median(a2,axis = 1))


a3 = np.array([[1,2],[3,4]])
a4 = np.array([[4,5],[6,7]])
a5 = np.array([[1,3,5],[4,2,7]])
a6 = np.array([[2,1,4],[4,2,1],[5,1,3]])
a7 = np.array([[4,2],[5,3]])

# print(a3 * a4) #cross product
# print(a3 @ a4) #dot product
# print(a3.dot(a4)) #dot product
# print(a5.transpose()) #transpose


# | 1 2 | = 1*4-2*3 = -2
# | 3 4 |
# print(np.linalg.det(a3))
# print(round(np.linalg.det(a6)))
# print(np.linalg.inv(a7))

# 3x = 9 
# [3] [X] = [9]


# a8 = np.array([[2]])
# b1 = np.array([90])

# x = np.linalg.solve(a8,b1)
# print(x)

# | 4x-3y = 1
# | 2x -y = -3

# a9 = np.array([[4,-3], [2,-1]])
# b2 = np.array([1,-3])

# hasil = np.linalg.solve(a9,b2)
# print(hasil)
# print('x= ', hasil[0])
# print('y= ', hasil[1])


# a10 = np.array([[7,2], [4,-3]])
# b3 = np.array([19,15])

# hasil = np.linalg.solve(a10,b3)
# print(hasil)
# print('x= ', hasil[0])
# print('y= ', hasil[1])
# print((3*hasil[0])-(2*hasil[1]))

#3persamaan

a11 = np.array([[1,1,-1], [1,2,1], [2,1,1]])
b4 = np.array([-3,7,4])

hasil = np.linalg.solve(a11,b4)
print(hasil)
print('x= ', hasil[0])
print('y= ', hasil[1])
print('z= ', hasil[2])

