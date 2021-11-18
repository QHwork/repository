from constant import autoan

class saveas_ang(object):
    def __init__(self):
        self = self
    def writein_ang(self,intcycle,X,V,Ek,num_of_eles,symb):
 
        if intcycle%5==0 : 
            print('Save Here')
            if intcycle == 0:
                print(intcycle)
            else:
                op_X = open(r'au/au_X'+str(intcycle)+'.au','w')
                op_V = open(r'au/au_V'+str(intcycle)+'.au','w')
                for i in range(intcycle-4,intcycle+1):
                    op_X.write('          '+str(num_of_eles)+'\n')
                    op_V.write('          '+str(num_of_eles)+'\n')
                    op_X.write('####### Ek='+str(Ek[i-1])+'#######\n')
                    op_V.write('####### Ek='+str(Ek[i-1])+'#######\n')
                    a = list(X[i])
                    b = list(V[i])
                    for j in range(num_of_eles):
                        c = list(a[j])
                        d = list(b[j])
                        op_X.write('{0:5}{1[0]:15.8f}{1[1]:15.8f}{1[2]:15.8f}\n'.format(symb[j],c))
                        op_V.write('{0:5}{1[0]:15.8f}{1[1]:15.8f}{1[2]:15.8f}\n'.format(symb[j],d))
                op_X.close()
                op_V.close()
            if intcycle == 200:
                op_200 = open(r'au/ang_X200.ang','w')
                for i in range(200):
                    op_200.write('        '+str(num_of_eles)+'\n')
                    op_200.write('####### Ek='+str(Ek[i-1])+'#######\n')
                    a = list(X[i]*autoan)
                    for j in range(num_of_eles):
                        c = list(a[j])
                        op_200.write('{0:5}{1[0]:15.8f}{1[1]:15.8f}{1[2]:15.8f}\n'.format(symb[j],c))
                op_200.close()                
                     
        else:
            print('No need to save')

          
