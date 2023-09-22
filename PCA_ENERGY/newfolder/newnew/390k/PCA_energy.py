import numpy as np
import pandas as pd
##
##
##varaiable has to be changed in the program,to create sub matrix from PCE
#ri==>row starting index
#rf==>row ending index
#ci==>coloumn starting index
#cf==>coloumn ending index



data1=pd.read_fwf("1p_vpgfg_390k.txt",header=None,names=["nos1","rog1","srog1"],sep=" ")
srog=np.array(data1["srog1"])

#print(srog)
#change the temperature titile for plots

ri=0
rf=1500
ci=2
cf=20

PCE=np.load("pcdata.npy")

nos=PCE[:,0]
energy=PCE[:,1]
xxx=PCE[0,:]
x=len(nos)
y=len(xxx)

y1=y-2
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

df=pd.DataFrame(PC)

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
pca=PCA(n_components=1)
pcafit=pca.fit_transform(fit)

newdf=pd.DataFrame(data=pcafit)
newdf=np.array(newdf)
#print(newdf)

p1c1e=[]
for i in range(x):
    pp=[]
    pp.append(srog[i])
    for j in range(1):  
        pp.append(newdf[i,j])
    pp.append(energy[i])
   
    p1c1e.append(pp)
    
###########################

p1c1e=np.array(p1c1e)  

   
pce270=pd.DataFrame(p1c1e)
pce270.to_csv('pce390k.csv', index=False,header=None)
#plt.show()


















