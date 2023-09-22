import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

####################################
# reading e2edata.npy numpy file and storing
# it into an array

e2e=np.load("e2edata.npy")
nos=len(e2e[:,0])

e2e=np.array(e2e).reshape(nos)



c,d=np.histogram(e2e,bins=20,density=True)
#c==> probability density
#d==> position of bins 
#e==> width of each bins

e=np.diff(d)
# this d is from histogram plot so contains one more element
# beacause histogram is plotted with x axis as width of the each bins
# hence considering an another array d1 which contains every elements except the first 
# this won't affect the plot bcz the width of the bin is small....
# simply we are relating width of the bin to the edge of the each bin.......


d1=[]
for i in range(len(d)-1):
     d1.append(d[i+1])
#print(d1)

#print(e)
#defining probabilty distribution
#distribution of probability is the product of the probability density and width of the each bins

pdis=c*e

lnpdis=np.log(pdis)
lnpdis=(-1)*lnpdis 
lnpdis=np.array(lnpdis)
k=1.380649*(10**-23)

for i in range(len(lnpdis)):
     
    lnpdis[i]=k*400*lnpdis[i]
#lnpdis contains  natural logrthimic (ln) of probability distribution of e2e

#print(lnpdis)


#######  d1 and lnpdis #######
lnpdisfit=np.polyfit(d1,lnpdis,2)
lnpdispoly=np.poly1d(lnpdisfit)

d1space=np.linspace(min(d1),max(d1),100)
lnpdis1=[]
for i in range(len(d1space)):
    lnp1=lnpdispoly(d1space[i])
    lnpdis1.append(lnp1)

#plt.title("Histogram plot of end to end distance 400k")
#plt.hist(e2e,bins=20,color="tan")
#plt.xlabel("ξ(Å)")
#plt.ylabel("counts")
#plt.show()


plt.subplot(1,2,1)
plt.title("F/KT vs ε (T=400k)",fontweight="bold")
plt.xlabel(" ξ(Å) - End to end distance",fontweight="bold")
plt.ylabel("F  Free energy in kcal/mol ",fontweight="bold")
plt.scatter(d1,lnpdis,color="tan")


plt.subplot(1,2,2)
plt.title("Fitted - F/KT vs ε (T=400k)",fontweight="bold")
plt.xlabel(" ξ(Å) - End to end distance",fontweight="bold")
plt.ylabel("F (J)  Free energy in kcal/mol ",fontweight="bold")
plt.scatter(d1space,lnpdis1,color="tan")
plt.show()
