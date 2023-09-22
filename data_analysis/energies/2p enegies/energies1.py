import numpy as np
import matplotlib.pyplot as plt

e111=np.load("energy270k.npy")
e222=np.load("energy300k.npy")
e333=np.load("energy340k.npy")
e444=np.load("energy380k.npy")

e11=[]
e22=[]
e33=[]
e44=[]
for i in range(1200):
       e11.append(e111[i])
       e22.append(e222[i])
       e33.append(e333[i])
       e44.append(e444[i])

e1=[]
e2=[]
e3=[]
e4=[]
for i in range(len(e11)):
               if e11[i]<100:
                  e1.append(e11[i])
               if  e22[i]<100:
                  e2.append(e22[i])
               if  e33[i]<100:
                  e3.append(e33[i])
               if  e44[i]<100:
                  e4.append(e44[i])



plt.title("Steepest energy")
plt.ylabel("Energy(J)")                  
plt.xlabel("Sample number")
plt.plot(e1,color="r")
plt.plot(e2,color="b")
plt.plot(e3,color="g")
plt.plot(e4,color="violet")
plt.legend(labels=["270k","300k","340k","380k"])
plt.show()
print(e1,e2,e3,e4)
