# Energy Landscape plot using PCA and Energy:
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib import cm
data = pd.read_csv("pce270k.csv",header=None)

dum_dat = pd.read_csv('EL_dumm.dat',header=None,delim_whitespace=True)
print(data)
print(dum_dat)

#Load data:
Zd = data.iloc[:,2]


for i in range(len(Zd)):
     if Zd[i]>0.0:
        Zd[i]=0.0
    # if Zd[i]<0.0:
       # Zd[i]=(-1)*Zd[i]
        
        
Xd = data.iloc[:,0]
Yd = data.iloc[:,1]


#Load dummy points:

Zdumm = dum_dat.iloc[:,2]
Xdumm = dum_dat.iloc[:,0]
Ydumm = dum_dat.iloc[:,1]

Zd = Zd.to_numpy()
Xd = Xd.to_numpy()
Yd = Yd.to_numpy()

Zdumm = Zdumm.to_numpy()
Ydumm = Ydumm.to_numpy()
Xdumm = Xdumm.to_numpy()

Z = np.hstack([Zd,Zdumm])
Y = np.hstack([Yd,Ydumm])
X = np.hstack([Xd,Xdumm])


minX = np.min(X)
maxX = np.max(X)
minY = np.min(Y)
maxY = np.max(Y)
minZ = np.min(Z)
maxZ = np.max(Z)


print(minZ)

#Create a meshgrid:
Xi,Yi = np.mgrid[minX:maxX:.37,minY:maxY:.37]

#Interpolate using griddata:

Zi = interpolate.griddata((X,Y),Z,(Xi,Yi),method='linear')
print(Xi)

#fig,ax = plt.subplots(1,1)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set(xlim=(minX, maxX), ylim=(minY, maxY))
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("Energy (Kcal/mol)")

plt.title("270k")


surf = ax.plot_surface(Xi,Yi,Zi,cmap=cm.coolwarm)

fig.colorbar(surf,shrink=0.6)





#for i in range(0,360):
#      ax.view_init(0,i)
##      plt.draw()
#      plt.pause(.001)
plt.savefig('Elan_cont.png')
plt.show()
