

file_name = "Koala.jpg"

import matplotlib.image as img
import matplotlib.pyplot as sav
import numpy as np
import sys


K = int(sys.argv[1])
#K_values = [2,5,10,15,20]

image = img.imread(file_name)
print(image.shape)

print(image[0].shape)

counter = 0
pixel_values = image.shape[0] * image.shape[1]
rgb = np.empty((pixel_values,3))
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        rgb[counter] = image[i][j]
        counter+=1
 
row, col = rgb.shape


print("For K:"+str(K))  
initial_centers = np.random.choice(rgb.shape[0],K,replace=None)
C_means = rgb[initial_centers]
distance_assign = np.empty(row)
#        dist = np.empty(K)
sums = np.zeros((K,col))
count = np.zeros(K).reshape(K,1)
compressed_rgb = np.empty((row,col))
for _ in range(10):
    
    def find_minimum(X):
        return np.argmin(np.linalg.norm((X - C_means), axis = 1))
    
    distance_assign = np.apply_along_axis(find_minimum, 1, rgb)

    for i in range(row):
       sums[int(distance_assign[i])] += rgb[i]
       count[int(distance_assign[i])] += 1
       
         
    C_means = sums / count           
    

for i in range(row):
    compressed_rgb[i] = C_means[int(distance_assign[i])]  
        
compressed_img = np.reshape(compressed_rgb,image.shape)
sav.imsave("Koala_compressed.jpg",compressed_img/255)