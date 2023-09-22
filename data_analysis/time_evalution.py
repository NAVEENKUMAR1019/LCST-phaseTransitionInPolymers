##########################
# decreasing order of energies is connected to increasing time evalution of th system
# e0==> energies of the samples
# e==>  decreasing order of energy 


import numpy as np
import matplotlib.pyplot as plt

ene=np.load("energiesdata.npy")
ene=np.array(ene)
e1=ene[:,2]
e0=[]
for i in range(len(e1)):
    e0.append(eval(e1[i]))
    
#print(t)
srog1=np.load("srogdata.npy")
srog=srog1[:,2]
e=np.array(e0)
srog=np.array(srog)



e=np.sort(e0)
e[::-1].sort()
#print(e)




####################
#  ordering srog   #         
####################
#o_srog===> ordered srog

 
o_srog=[]

for i in range(len(e)):

    for j in range(len(e0)):
                 if e[i]==e0[j]:
                      kk=srog[j]
    o_srog.append(kk)
    
    
o_srog=np.array(o_srog)      
#print(e,e1)
#print(o_srog)          


plt.title("390k")
plt.xlabel("Number of samples")
plt.ylabel("<Srog>")
plt.plot(o_srog)
plt.show()                 


np.save("energy390k",e)


