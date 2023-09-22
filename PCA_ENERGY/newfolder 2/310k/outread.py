import numpy as np

file = open("2p-elp_clp_310k_1-1500_mini.out",'r')

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
    if len(l) < 5:
        l.append(0)
    if len(l) < 5:
        l.append(0)
    if len(l)<5:
        l.append(0) 
    if len(l)<5:
        l.append(0)


    newdata.append(l)

newdata = newdata[:-1]

ndata = np.array(newdata).reshape(1500,35)
np.save("pcdata.npy",ndata)



#print(ndata)

#print(ndata.dtype)

