#! /bin/bash
find . -name 'for_TS' > findTS
sed -i 's/for_TS//g' findTS
mkdir TS_
#file=$*
file=`cat findTS`
cd TS_
for i in $file
do
mkdir ${i}
done 
for i in *
do
echo ${i} >> forTS_ls
done
file=`cat forTS_ls`
cd ..
for i in $file
do
cd ${i}
ls *.gjf > gjf_forTS
sed -i 's/gmodel//g' gjf_forTS
sed -i 's/.gjf//g' gjf_forTS
awk '{print $1}' for_TS > for_TS_forTS
cp ../move_TSopt.py .
python3 move_TSopt.py
files=`cat forTS_cp`
for j in $files
do
# change here
cp ../../workspace_merge/${i}/gauss_tmp/${j} ../TS_/${i}/
sed -i '1d' ../TS_/${i}/${j}
sed -i '4c # opt=(calcFC,recalc=7,ts,noeigen) b3lyp/6-31g(d,p) scf=maxcycle=1024' ../TS_/${i}/${j}
done
cd ..
done
cd TS_
find . -name '*.gjf' > for_run
cp ../job.sh .
