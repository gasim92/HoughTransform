from PIL import Image,ImageFilter,ImageDraw
import numpy as np
import math
#Hough Transform 
#xcons(teta)+ysin(teta)=p


#Load image 
img=Image.open("input/triangle_1.png")
img_gray=img.convert("L")
img_shape=img_gray.size
hough=np.zeros(img_shape,dtype=int)

#use edege detection
edge = np.array(img_gray.filter(ImageFilter.FIND_EDGES))
edge_numpy=Image.fromarray(edge)

edge[edge<255]=0
edge_numpy.save("output/edge.png")

#generate p and teta space
for i in range(img_shape[0]):
    for j in range(0,img_shape[1]):
        if (edge[i,j]==255):
            #print(i,j,"    ",edge[i,j])
            #this is an edge and x,y
            for teta in range (0,img_shape[1]):
                p=j*np.cos(teta)+i*np.sin(teta)
                hough[int(teta),int(p)]+=1
        else:
            continue

print(hough)
#Image.fromarray(hist).show
#hough[hough<100]=0
#HT=Image.fromarray(hough)
#HT.save("output/hough.png")
#HT.show()


    
    
