import csv
import matplotlib.pyplot as plt
import numpy as np

data = []
prov = []
rokok15 = []
rokok16 = []
# x2 = [1,2,3,4,5,6,7,8,9]
with open('rokok.csv','r') as fileku:
    reader = csv.reader(fileku)
    for x in reader:
        prov.append(x[0])
        rokok15.append(float(x[1]))
        rokok16.append(float(x[2]))

prov.remove(prov[0])
rokok15.remove(rokok15[0])
rokok16.remove(rokok16[0])

rokok15 = np.array(rokok15)
rokok16 = np.array(rokok16)

mean15 = np.mean(rokok15)
mean16 = np.mean(rokok16)
mean15new = []
mean16new = []

for x in range (len(rokok15)-1):
    mean15new.append(mean15)

for x in range (len(rokok16)-1):
    mean16new.append(mean16)

provup = []
rokok15up = []
rokok16up = []
mean15shape = []
mean16shape = []

for i in range(len(rokok15)-1):
    if rokok15[i] > mean15new[i] and mean16new[i]<rokok16[i] and rokok16[i]<rokok15[i]:
        provup.append(prov[i])
        rokok15up.append(rokok15[i])
        rokok16up.append(rokok16[i])
        mean15shape.append(mean15new)
        mean16shape.append(mean16new)

mean15shape = np.array(mean15shape)
mean16shape = np.array(mean16shape)
print(mean15shape.shape)
print(mean16shape.shape)

# print(prov)
# print(rokok15)
# print(rokok16)
# print(np.mean(rokok15))


# plt.bar(prov, rokok15)
# plt.bar(prov, rokok16)

plt.bar(provup, rokok15up)
plt.bar(provup, rokok16up)
plt.plot(provup, mean15shape)
plt.plot(provup, mean16shape)


# for x in reader:
# plt.plot(,np.mean(rokok15),'r--')


plt.xticks(rotation=90)
# plt.yticks(np.arange(34))
plt.yticks(np.arange(0,34,step=5))
plt.legend(['2015','2016']) #,loc=x
plt.show()

