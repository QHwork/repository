#! /bin/usr/python3
import os
import time

fp = open('Normal','r').read().splitlines()
for i in range(len(fp)):
    route = fp[i]
    mv = '''`cd {route}; python3 distance_graph_matrix.py; cd ..`'''
    os.system(mv.format_map(vars()))
