import numpy as np

file = open("radius_of_gyration.txt",'r')

with file as src:
    fl = src.read()
lines = fl.split('\n')

newdata = []

# Reading a single line and extracting data
for oneline in lines:
   # split the line with spaces
    onedata = oneline.split(' ')
    l = [] # line
    # remove element if nothing
    for k in onedata:
        if k == '':
            continue
        else: 
            l.append(eval(k))

    newdata.append(l)

newdata = newdata[:-1]

ndata = np.array(newdata)
np.save("srogdata.npy",ndata)



#print(ndata)

#print(ndata.dtype)







