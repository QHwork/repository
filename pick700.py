#! /bin/usr/python3
import os
import random
import numpy as np
wanted_points = np.loadtxt('points')
points = []
points_i = []
while len(points_i)<700:
    random_i = random.randint(0,len(wanted_points)-1)
    if random_i not in points_i:
        points_i.append(random_i)
        points.append(wanted_points[random_i])
np.savetxt('700points',points,fmt='%0.8f')

wanted_points_coor = np.loadtxt('xyz.txt')
points_coor = []
for i in range(len(points)):
    points_coor.append(wanted_points_coor[int(points[i])])
points_coor = np.array(points_coor)
np.savetxt('700points_coor',points_coor)

