#encoding:utf-8

#!/usr/bin/env python 

import os
import re
import sys
import datetime
import numpy as np

def softname(softname):
    softall = {'gaussian':gaussian()}
    if softname not in softall:
        #print('Plz use useful keyword')
        exit(1)
    return softall.get(softname)

class gaussian():
    def __init__(self):
        self = self
    def runsoft(self,ready_forrun_file,open_file_mode,intcycle):
        outname = ready_forrun_file.split('.')[0] + '.log'       
        if open_file_mode == 'r':
            os.system('g16 %s' %ready_forrun_file)
        return outname

if __name__ == '__main__':
    soft_name = 'gaussian'
    intcycle = 0
    softname(soft_name)
    #print(softname(soft_name).runsoft('test0.gjf','r',intcycle))
