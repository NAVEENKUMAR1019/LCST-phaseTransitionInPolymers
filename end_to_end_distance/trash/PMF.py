import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import normal
from numpy import std 
from scipy.stats import norm
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

####################################
# reading e2edata.npy numpy file and storing
# it into an array


e2e=np.load("e2edata.npy")

nos=len(e2e[:,0])

e2e=np.array(e2e).reshape(nos)
plt.hist(e2e,bins=10)
plt.show()

c,d=np.histogram(e2e,bins=20,density=True)
#c==> probability density(10)
#d==> position of bins (11)
#e==> width of each bins

#print(c)
#print(d)
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

#sns.kdeplot(e2e)
#print(sum(pdis))
#print(pdis)

lnpdis=np.log(pdis)
lnpdis=(-1)*lnpdis
#print(lnpdis)

#lagrangian interpolation

#lnspace=np.linspace(min(d1)+5,max(d1)-5,50)

#print(d1)
#print(lnpdis)
#d1==>x[i]
#lnpdis==>y[i]



#n=len(d1)
#
#lnpdis1=[]
#for h in range(len(lnspace)):
#    p=1
#    lp=0
#    for i in range(3,n-3):
#          for j in range(3,n-3):
#               if i!=j:
#                   p =  p*(lnspace[h]-d1[j])/(d1[i]-d1[j])
#          lp = lp + p*lnpdis[i]
#    lnpdis1.append(lp)        


#poly=lagrange(d1,lnpdis)
#lnp=Polynomial(poly)
#
#print(lnp(3))


#lnpp=[]
#for i in range(len(lnspace)):
#    for j range(len(lnp)):
#       lnpp[i] +=lnp[j]*lnspace[i]
 #      print(lnp)
#


print(lnpdis1)
#lnpdis contains  natural logrthimic (ln) of probability distribution of e2e

plt.subplot(1,2,1)
plt.title("F/KT vs ε (T=270k)",fontweight="bold")
plt.xlabel(" ε(Å) - End to end distance")
plt.ylabel("F/KT")




plt.scatter(d1,lnpdis)


plt.show()
