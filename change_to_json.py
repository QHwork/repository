import numpy as np
import matplotlib.pyplot as plt
import copy
import math
import cmath
import os
import shutil
import json
import sub_interface_json

class w_r_json(object):
    def __init__(self):
        self = self
    def create_dir(self,path):
        try:
            shutil.rmtree(path)
            os.makedirs(path)
        except:
            os.makedirs(path)

    def input_to_json_file (self,input_file, json_file) :
        xxx = sub_interface_json.read_data_with_label (input_file)
        sub_interface_json.dump_json(json_file, xxx)

    def read_from_json (self,json_file) :
        para_all = sub_interface_json.load_json(json_file)
        return para_all

if __name__ == '__main__':
    WRj = w_r_json()
    WRj.input_to_json_file('tmp_file_para_all.txt','tmp_paraall_json.json')
    #print(WRj.read_from_json('tmp_paraall_json.json'))