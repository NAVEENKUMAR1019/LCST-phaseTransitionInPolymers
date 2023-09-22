import numpy as np
import pandas as pd
##
##
##varaiable has to be changed in the program,to create sub matrix from PCE
#ri==>row starting index
#rf==>row ending index
#ci==>coloumn starting index
#cf==>coloumn ending index

#change the temperature titile for plots

ri=0
rf=1500
ci=2
cf=35








#PCE====>this matrix contains all component and energy
PCE=np.load("pcdata.npy")

nos=PCE[:,0]
energy=PCE[:,1]
xxx=PCE[0,:]
x=len(nos)
y=len(xxx)

#for PC matrix there is no nos and energy coloumn 
#so number of coloumn is reduced by a factor of 2
y1=y-2


#PC======> this matrix contains only components
PC=[]

for i in range(ri,rf):
     h=[]
     for j in range(ci,cf):
         h.append(PCE[i,j])
     PC.append(h)     
     
PC=np.array(PC)
for i in range(x):
    for j in range(y1):
        if PC[i,j] < 0.0 :
           PC[i,j]=PC[i,j]+360.0



#print(PC)   
#print(PC.shape)

#creating a pandas dataframe
df=pd.DataFrame(PC)
#print(df)

####################################################################################
#                                                                                  #
#                                                                                  #
#                                                                                  #
#             PRINCIPAL COMPONENT  ANALYSIS                                        #
#                                                                                  #
#                                                                                  #
####################################################################################

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits import mplot3d
from matplotlib import cm

from matplotlib.animation import FuncAnimation as fa
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler




scaler=StandardScaler()

fit=scaler.fit_transform(df)
pca=PCA(n_components=2)
pcafit=pca.fit_transform(fit)

newdf=pd.DataFrame(data=pcafit)
newdf=np.array(newdf)
#print(newdf)

p1c1e=[]
for i in range(x):
    pp=[]
    for j in range(2):  
        pp.append(newdf[i,j])
    pp.append(energy[i])
    p1c1e.append(pp)

###########################

p1c1e=np.array(p1c1e)  
#plt.scatter(p1c1e[:,0],p1c1e[:,1])
#plt.xlabel("PC1")
#plt.ylabel("PC2")
#plt.title("PC1 vs PC2 (380k)")
#plt.show()


p1c1e=np.array(p1c1e)  
#plt.hist2d(p1c1e[:,0],p1c1e[:,1],bins=(30,30))
#plt.xlabel("PC1")
#plt.ylabel("PC2")
#plt.title("PC1 vs PC2 (380k)")
#plt.colorbar()
#plt.show()




##########################
#                        #
#     3D PLOTTING        #
#                        #
##########################


#print(p1c1e)
#plotting
fig=plt.figure()
ax=plt.axes(projection="3d")





####observed plot is dominated by higher energies 
#so removing higer energies
p1c1e1=[]
for i in range(x):
    looo=[]
    if p1c1e[i,2]<0:        
        looo.append(p1c1e[i,0])
        looo.append(p1c1e[i,1])
        looo.append(p1c1e[i,2])
        p1c1e1.append(looo)

p1c1e1=np.array(p1c1e1)




#3d hue plotting

c_map=plt.get_cmap("hsv")
x=p1c1e1[:,0]
y=p1c1e1[:,1]
z=p1c1e1[:,2]



plt.title("380k",fontweight="bold")
ax.set_xlabel("PC1",fontweight="bold")
ax.set_ylabel("PC2",fontweight="bold")
ax.set_zlabel("energy in J/Mol",fontweight="bold")
#ax.scatter3D(x,y,z,alpha=1,c=(x+y+z),cmap=c_map,marker="s")

#for i in range(0,360):
 #     ax.view_init(0,i)
  #    plt.draw()
   #   plt.pause(.001)
   
pce270=pd.DataFrame(p1c1e)
pce270.to_csv('pce330k.csv', index=False,header=None)
#plt.show()


















