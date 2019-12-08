import numpy as np
    
print('')
print ('Enter the corresponding x value in a bracket that aligns to its corresponding y value on another bracket')
print ('Example: for points (1,2) and (3,4) enter [1,3] and [2,4]')
print ('')
xval = eval(input('Enter X Values in a bracket []: '))
yval = eval(input('Enter Y Values in a bracket []: '))

xarray = np.array([(xval)])
yarray = np.array([(yval)])

xtrans = np.transpose(xarray)
ytrans = np.transpose(yarray)

point = np.column_stack((xtrans,ytrans))  

n = len(point)  

for i in range(n):
    
    P = np.polyfit(point[:,0], point[:,1],i)
    F = np.polyval(P, point[:,0])
    e = np.linalg.norm(point[:,1] - F)
        
    x = [i,e]
        
    if i==0:
        y = x
            
    elif y[1] >= x[1]:
            
        z = x[0]
            
p = np.polyfit(point[:,0],point[:,1],z)

print('The Coefficients are:',p)

