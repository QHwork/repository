#! /bin/usr/python3
import numpy as np
import os
import math
import time
import random
from collision import plus_v1,plus_v2


pi = np.pi
cos = np.cos
sin = np.sin
arccos = np.arccos
arcsin = np.arcsin
degrees = np.degrees
def sphere():
    r = 1
    X = []
    Y = []
    Z = []
    for i in range(500):
        phi = random.uniform(0,pi)
        theta = random.uniform(0,2*pi)
        x = r*sin(phi)*cos(theta)
        y = r*sin(phi)*sin(theta)
        z = r*cos(phi)
        X.append(x)
        Y.append(y)
        Z.append(z)

    X = np.array(X) 
    #X = x.tolist()
    Y = np.array(Y)
    #Y = y.tolist()
    Z = np.array(Z)
    #Z = z.tolist()

    np.savetxt('x2.txt',X,fmt='%0.8f')
    np.savetxt('y2.txt',Y,fmt='%0.8f')
    np.savetxt('z2.txt',Z,fmt='%0.8f')

    os.system('''`paste x2.txt y2.txt z2.txt > xyz2.txt`''')
    sphere = np.loadtxt('xyz2.txt')
    return sphere

def rotate_mv(traj_i,num2,surface_point,sphere):
    os.system('''`bash for_rotate_coor2.sh`''')
    time.sleep(1)
    h2o_coor = np.loadtxt('h2o_coor.txt')
    h2o_reaction_center = []
    a = 0
    s = 0
    d = 0
    for i in h2o_coor:
        a += i[0]
        s += i[1]
        d += i[2]
    h2o_reaction_center.append(a/num2)
    h2o_reaction_center.append(s/num2)
    h2o_reaction_center.append(d/num2)

    h2o_coor_mv2center = h2o_coor
    #print(h2o_coor)
    for i in range(len(h2o_coor)):
        h2o_coor_mv2center[i] = h2o_coor[i] - h2o_reaction_center
    #print(h2o_coor_mv2center)

    random_label = []
    for i in range(len(sphere)):
        random_label.append(random.randint(0,len(sphere)-1))

    random_label_copy = []
    for i in range(len(sphere)):
        random_label_copy.append(random.randint(0,len(sphere)-1))


    random_i = random_label[0]
    I = np.identity(3)
    A0 = sphere[random_i]
    #print(A0)
    A1 = np.array([[A0[0]*A0[0],A0[0]*A0[1],A0[0]*A0[2]],[A0[1]*A0[0],A0[1]*A0[1],A0[1]*A0[2]],[A0[2]*A0[0],A0[2]*A0[1],A0[2]*A0[2]]])
    A2 = np.array([[0,-A0[2],A0[1]],[A0[2],0,-A0[0]],[-A0[1],A0[0],0]])
    random_theta = random.uniform(0,2*pi)
    M = A1 + cos(random_theta)*(I-A1)+sin(random_theta)*A2
    #print(M)
    Mt = np.transpose(M)
    #print(Mt)
    h2o_coor_new = np.dot(h2o_coor_mv2center,Mt)
    #print(h2o_new)
    for i in range(len(h2o_coor_new)):
        h2o_coor_new[i] = h2o_coor_new[i] + surface_point 
    np.savetxt('h2o_coor_center_rotate.txt',h2o_coor_new,fmt='%0.8f')



    #################### # Velocity # ###################
    os.system('''`bash for_rotate_vel2.sh`''')
    time.sleep(1)
    h2o_vel = np.loadtxt('h2o_vel.txt')
    #print(len(h2o_vel))
    h2o_vel_new = np.dot(h2o_vel,Mt)
    #print(len(h2o_vel_new))

    v1_direction = np.array(surface_point) 
    v2_direction = np.array(surface_point*(-1))
    sum_direction = surface_point[0]**2+surface_point[1]**2+surface_point[2]**2
    sqrt_direction = math.sqrt(sum_direction)
    plus_Ekc_v1 = plus_v1/sqrt_direction*v1_direction
    plus_Ekc_v2 = plus_v2/sqrt_direction*v2_direction

    for i in range(len(h2o_vel_new)):
        h2o_vel_new[i] = h2o_vel_new[i] + plus_Ekc_v2
    np.savetxt('h2o_vel_rotate.txt',h2o_vel_new,fmt='%0.8f')


    ################### # khf # #########################
    os.system('''`bash mv_for_BOMD.sh`''')
    time.sleep(1)
    khf_coor = np.loadtxt('khf_coor.txt')
    khf_reaction_region_center = np.loadtxt('khf_reaction_region_center.txt')
    for i in range(len(khf_coor)):
        khf_coor[i] = khf_coor[i] - khf_reaction_region_center
    np.savetxt('khf_coor_mv.txt',khf_coor,fmt='%0.8f')
    
    khf_vel = np.loadtxt('khf_vel.txt')
    for i in range(len(khf_vel)):
        khf_vel[i] = khf_vel[i] + plus_Ekc_v1
    np.savetxt('khf_vel_mv.txt',khf_vel,fmt='%0.8f')

    return


if __name__ == '__main__':
    sphere = sphere()
    num2 = np.loadtxt('num2')
    mv_2_surface = np.loadtxt('700points_coor')
    for traj_i in range(1,701):
        op = open('traj_i','w')
        op.write(str(traj_i))
        op.close()
        time.sleep(1)
        surface_point = mv_2_surface[traj_i-1]
        rotate_mv(traj_i,num2,surface_point,sphere)
        os.system('''`bash change_name.sh`''')
        time.sleep(1)
