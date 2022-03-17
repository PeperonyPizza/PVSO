import numpy as np
import matplotlib.pyplot as plt


def vote_acumulator(img):

    height, width = img.shape  # velkost obrazka - vyska sirka
    thetas=np.deg2rad(np.arange(-90,90,1))
    diagonala=int(np.sqrt((height*height)+(width*width)))
    rhos=np.arange(-diagonala,diagonala,1)
    acc=np.zeros((len(rhos),len(thetas)),dtype=np.uint64)
    akumulator1=np.zeros((len(rhos),len(thetas)),dtype=np.uint64)
    indexy,indexx=np.nonzero(img)
    print(indexx,indexy)
    for i in range(len(indexy)):
        for j in range(len(thetas)):
            ro=int(diagonala+indexx[i]*np.cos(thetas[j])+indexy[i]*np.sin(thetas[j]))
            acc[ro, j]+=1
            
        
    return acc,rhos,thetas

