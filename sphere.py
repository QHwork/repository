#! /bin/usr/python3
import os
import numpy as np

#create a sphere
r = 7
pi = np.pi
cos = np.cos
sin = np.sin
phi,theta = np.mgrid[0.0:pi:100j,0.0:2*pi:200j]
x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)

#in this way ull get a array((1,10,10))
x = x.reshape((20000,1))
#X = x.tolist()
y = y.reshape((20000,1))
#Y = y.tolist()
z = z.reshape((20000,1))
#Z = z.tolist()


np.savetxt('x.txt',x,fmt='%0.8f')
np.savetxt('y.txt',y,fmt='%0.8f')
np.savetxt('z.txt',z,fmt='%0.8f')

os.system('''`paste x.txt y.txt z.txt > xyz.txt`''')
os.system('''`rm x.txt y.txt z.txt`''')

