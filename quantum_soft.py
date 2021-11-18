import load_X_as_softinput
import softapi
import get_log
import importlib
import numpy as np
from constant import autoan

class quantum_soft():
    def __init__(self):
        self = self

    def get_para(self):
        dictionary = {'gaussian':'softapi'}
        a = importlib.import_module('Get_all_to_json')
        para_all = a.get_all_to_json().get_to_json()
         
        if para_all['softused'] in dictionary:
            c = importlib.import_module(dictionary[para_all['softused']])
        else:
            print('Sorry man,this software has not been supported yet!')
        return para_all,c

    def soft_initial(self):
        #print('This is the soft\'s initial run for Force!')
        para_all,c = self.get_para()

        LdX = load_X_as_softinput.load_for_soft()
        Gl = get_log.get_log()
        b = importlib.import_module('read_for_DD')

        symb,X_0,V_0,X,V,dt,num_of_eles,intcycle,numcycle,filename,softused = b.read_to_DD().select_needed_info(para_all)
        X_0 = np.array(X_0,dtype=float)
        X_0 = X_0*autoan

        new_gjf_name = LdX.writein_gjf(r'gauss_tmp/model',X_0,intcycle,num_of_eles,symb)
        gauss = softapi.softname(softused)
        outname = gauss.runsoft(new_gjf_name,'r',intcycle)

        Fi = Gl.get_forces(outname,intcycle,num_of_eles)
        Evi = Gl.get_Ev(intcycle,outname)
        force_filename = Gl.update_force(intcycle,Fi,r'tmp/tmp_force_json.json')
        Ev_filename = Gl.upload_Ev(r'tmp/tmp_Ev_json.json',intcycle,Evi)
        F = b.read_to_DD().load_new_json_to_trans(force_filename,intcycle)
        return F

    def soft_loop(self,X,intcycle,num_of_eles,symb,softused):
        LdX = load_X_as_softinput.load_for_soft()
        Gl = get_log.get_log()
        b = importlib.import_module('read_for_DD')

        coordiantes = LdX.get_coordinates(X,intcycle)
        new_gjf_name = LdX.writein_gjf(r'gauss_tmp/gmodel',coordiantes,intcycle,num_of_eles,symb)
        gauss = softapi.softname(softused)
        outname = gauss.runsoft(new_gjf_name,'r',intcycle)
        Fi = Gl.get_forces(outname,intcycle,num_of_eles)
        Evi = Gl.get_Ev(intcycle,outname)
        force_filename = Gl.update_force(intcycle,Fi,r'tmp/tmp_force_json.json')
        Ev_filename = Gl.upload_Ev(r'tmp/tmp_Ev_json.json',intcycle,Evi)
        F = b.read_to_DD().load_new_json_to_trans(force_filename,intcycle)
        return F


