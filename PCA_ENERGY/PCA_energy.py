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
cf=20








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
plt.hist2d(p1c1e[:,0],p1c1e[:,1],bins=(30,30))
plt.xlabel("PC1",fontweight="bold")
plt.ylabel("PC2",fontweight="bold")
plt.title("PC1 vs PC2 (350 K)",fontweight="bold")
plt.colorbar()
plt.show()
















