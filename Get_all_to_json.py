import importlib
class get_all_to_json(object):
    def __init__(self):
        self = self
    def get_to_json(self):
        a = importlib.import_module('read_input_coor_vel')
        b = importlib.import_module('change_to_json')

        inputed_data = a.get_input().get_info_from_input('input.inp')
        X_0,symbol = a.get_X_0().get_init_coordinate('coordinate.txt')
        v_0 = a.get_v_0().get_init_velocity('velocity.txt')
        init_all_file = a.para_data_X_v().write_in_file(inputed_data,X_0,symbol,v_0)
        
        b.w_r_json().create_dir(r'tmp/')
        b.w_r_json().create_dir(r'au/')
        b.w_r_json().input_to_json_file(init_all_file,r'tmp/tmp_paraall_json.json')
        para_all = b.w_r_json().read_from_json(r'tmp/tmp_paraall_json.json')
     
        return para_all


if __name__ == '__main__':
    Ga = get_all_to_json()
    #print(Ga.get_to_json)
