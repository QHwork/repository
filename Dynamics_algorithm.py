import importlib
import quantum_soft
import save_update

class dynamics_algorithm(object):
    def __init__(self):
        self = self
    def get_para(self):
        dictionary = {'velocity_verlet':'velocity_verlet_algorithm','runge_kuta':'RK4'}
        a = importlib.import_module('Get_all_to_json')

        para_all = a.get_all_to_json().get_to_json()
       
        if para_all['algorithm'] in dictionary:
            c = importlib.import_module(dictionary[para_all['algorithm']])
        else:
            print('Sorry,this algorithm has not been supported yet!')
        return para_all,c
    def mainloop(self):

        b = importlib.import_module('read_for_DD')
        para_all,c = self.get_para()
        symb,X_0,V_0,X,V,dt,num_of_eles,intcycle,numcycle,filename,softused = b.read_to_DD().select_needed_info(para_all)

        Qs = quantum_soft.quantum_soft()
        save_up = save_update.save_update()


        Ek = []
        for intcycle in range(numcycle):
            if intcycle == 0:
                #print('This is the first loop of Mainloop!')
                F = Qs.soft_initial()
            v_half = c.vel_ver().v_v_half_velocity(V,F,intcycle,dt,num_of_eles,symb)
            intcycle += 1
            X = c.vel_ver().v_v_coordinates(X,F,v_half,symb,num_of_eles,dt,intcycle)
            F = Qs.soft_loop(X,intcycle,num_of_eles,symb,softused)
            V = c.vel_ver().v_v_velocity(V,F,dt,intcycle,v_half,num_of_eles,symb)
            Ek.append(c.vel_ver().v_v_kineticE(V,symb,intcycle))
            #print(intcycle)
            save_up.saveup(intcycle,X,V,Ek,num_of_eles,symb)
        #print(len(Ek))
   
        




if __name__ == '__main__':
    MD = dynamics_algorithm()
    MD.mainloop()




