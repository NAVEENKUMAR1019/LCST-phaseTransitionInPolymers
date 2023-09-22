  
##################  this folder creates necessary data for three dimensional energy landscape polting##########


this folder takes the .out file which contains energy and dihedral angles of simulated structures 

1)PCA - principal component analysis several dihedral degrees of freedom is reduced to two component 
                     pca1 and pca2
2)energy of eacch structure is notes and three dimensional energy landscape is created 
                  
                  pca1 and pca2 are in x and y axis

                  energy of the structure in z axis

3)3 dimensional surface is created by representing energy as a function if pca1 and pca2
                    
                   this is achieved by legrangian interpolation of 2 variables             

steps:::::::::::::::::::

 1) outread.py read the ********.out file and returns a numpy file 
called pcdata.npy
this numpy file can be imported and easily accessed using numpy functions






 
