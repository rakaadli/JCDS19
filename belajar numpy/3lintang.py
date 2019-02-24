import csv
import numpy as np
import matplotlib.pyplot as plt

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

plt.bar(provover,rokok15over)
plt.bar(provover,rokok16over)
plt.plot(provover,np.repeat(ratarokok15,len(provover)), 'g-', linewidth=3)
plt.plot(provover,np.repeat(ratarokok16,len(provover)), 'g-', linewidth=3)
plt.ylim(25,35)
plt.xticks(rotation=90)
plt.legend(['2015','2016'])
plt.show()