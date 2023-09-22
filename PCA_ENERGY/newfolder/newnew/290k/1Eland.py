# Energy Landscape plot using PCA and Energy:
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib import cm
data = pd.read_csv("pce290k.csv",header=None)

dum_dat = pd.read_csv('EL_dumm.dat',header=None,delim_whitespace=True)
#print(data)
#print(dum_dat)

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


#print(minZ)

#Create a meshgrid:
Xi,Yi = np.mgrid[minX:maxX:.37,minY:maxY:.37]

#Interpolate using griddata:

Zi = interpolate.griddata((X,Y),Z,(Xi,Yi),method='linear')


#fig,ax = plt.subplots(1,1)
#fig = plt.figure()
#ax = plt.axes(projection='3d')

vmin=-200
vmax=0


fig,ax = plt.subplots(1,1)


ax.set(xlim=(-3,3), ylim=(-3,3))
ax.set_xlabel("PC1",fontweight="bold")
ax.set_ylabel("PC2",fontweight="bold")
#ax.set_zlabel("Energy (Kcal/mol)")

plt.title("290k",fontweight="bold")

surf = ax.contourf(Xi,Yi,Zi,cmap=cm.seismic,vmin=vmin,vmax=vmax)


fig.colorbar(surf,shrink=1.0,  ticks=range(vmin, vmax+20,20))
plt.savefig('contour290k.png')
plt.show()

