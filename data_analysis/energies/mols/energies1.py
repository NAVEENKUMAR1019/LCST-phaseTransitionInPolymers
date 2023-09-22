import numpy as np
import matplotlib.pyplot as plt

e11=np.load("energy270k.npy")
e22=np.load("energy310k.npy")
e33=np.load("energy350k.npy")
e44=np.load("energy390k.npy")


e1=[]
e2=[]
e3=[]
e4=[]
for i in range(len(e11)):
               if e11[i]<0:
                  e1.append(e11[i])
               if  e22[i]<0:
                  e2.append(e22[i])
               if  e33[i]<0:
                  e3.append(e33[i])
               if  e44[i]<0:
                  e4.append(e44[i])



plt.title("Mols optimal structures (energies < 0 kcal/mol)",fontweight="bold")
plt.ylabel("Energy (Kcal/mol)",fontweight="bold")                  
plt.xlabel(" Number of sample",fontweight="bold")
plt.plot(e1,color="r")
plt.plot(e2,color="b")
plt.plot(e3,color="g")
plt.plot(e4,color="violet")
plt.legend(labels=["270 K","310 K","350 K","390 K"])
plt.show()
#print(e1,e2,e3,e4)
