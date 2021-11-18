#! /bin/bash
path=`pwd`
Dpath=$path
merge_path=workspace_merge
num1=`cat num1`
tail -$num1 $Dpath/$merge_path/1/stru_xyz.in_1 | awk -F " " '{print $1}' > sym1
num2=`cat num2`
tail -$num2 $Dpath/$merge_path/1/stru_xyz.in_2 | awk -F " " '{print $1}' > sym2
