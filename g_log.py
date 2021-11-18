#! /bin/usr/python3
import os
os.system('''`bash g_sym.sh`''')
fp = open('for_run','r').read().splitlines()
fw = open('for_TS','a')
a = []
b = []
c = []
for i in range(len(fp)):
    fp_0 = fp[i].split('/')[0]
    fp_01 = fp[i].split('/')[1]
    fp_1 = fp_01.strip('gmodel')
    fp_2 = fp_1.strip('.gjf')
    fp_2 = int(fp_2)
    a.append(fp_0)
    b.append(fp_2)
    if i >= 1:
        if a[i] == a[i-1]:
            if i == 1:
                c.append(b[i-1])
            c.append(b[i])
        else:
            c.sort(reverse=False)
            for j in range(len(c)):
                w_content = a[i-1]+'/gmodel'+str(c[j])+'.log'
                fw.write(w_content+'\n')
            c = []    
            c.append(b[i])
fw.close()
print('done')
fp1 = open('for_TS','r').read().splitlines()
for i in range(len(fp1)):
    fp1_0 = fp1[i].split('/')[0]

    sed_i = 'log_file='+fp1[i]
    sed_1 = '''`sed -i '2c {sed_i}' g_log.sh`'''
    fp1_1 = 'coor_file='+fp1_0+'/coor_all'
    sed_2 = '''`sed -i '3c {fp1_1}' g_log.sh`''' 
    os.system(sed_1.format_map(vars()))
    os.system(sed_2.format_map(vars()))
    b_sh = '''`bash g_log.sh`''' 
    os.system(b_sh.format_map(vars()))
