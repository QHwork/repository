#! /bin/bash
num_sum=`cat num_sum`
num_add1=`expr $num_sum + 8`
num_add2=`expr $num_sum + 4`
cp for_run for_disTS
sym=$(head -1 for_run)
# change here
head -$num_add1 $sym | tail -$num_sum | awk '{print $1}' > sym_all
sed -i 's/gjf/log/g' for_disTS
log=`cat for_disTS`
A="Normal"
for i in $log
do
	normal=`tail -1 ${i}`
	if [[ $normal == *$A* ]]
	then
		echo ${i} >> normal_TS
                # change here
                sed -n '/Standard orientation/,+'$num_add2'p' ${i} | tail -$num_sum | awk '{print $4"\t"$5"\t"$6}' >> coor_all
	else
		echo ${i} >> disnormal_TS
        fi
done
python3 disTS.py > TSversion_all
