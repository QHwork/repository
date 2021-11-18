#易中君子，定卦省身#
#! /bin/bash
path=`pwd`
Dpath=$path
merge_path=workspace_merge
num01=`sed -n '$=' $Dpath/$merge_path/1/stru_xyz.in_1`
num1=`expr $num01 - 2`
echo $num1 > num1
num02=`sed -n '$=' $Dpath/$merge_path/1/stru_xyz.in_2`
num2=`expr $num02 - 2`
echo $num2 > num2
num_sum=`expr $num1 + $num2`
echo $num_sum > num_sum
