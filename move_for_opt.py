#! /bin/usr/python3
import os
fp = open('for_run','r').read().splitlines()
for i in range(len(fp)):
    fp_0 = fp[i].split('/')[0]
    fp_1 = fp[i].split('/')[1]
    fp0 = '''`mkdir {fp_0}`'''
    fp1 = '''`cp ../workspace_merge/{fp_0}/gauss_tmp/{fp_1} {fp_0}/`'''
    os.system(fp0.format_map(vars()))
    os.system(fp1.format_map(vars()))
for i in range(len(fp)):
    fp2 = fp[i]
    fp_sed = '''`sed -i '1d' {fp2}`'''
    os.system(fp_sed.format_map(vars()))
for i in range(len(fp)):
    fp3 = fp[i]
    fp_sed2 = '''`sed -i '4c # hf/3-21g opt=(calcFC) scf=maxcycle=1024' {fp3}`'''
    os.system(fp_sed2.format_map(vars()))


