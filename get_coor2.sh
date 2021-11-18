#! /bin/bash
path=`pwd`
Dpath=$path
merge_path=workspace_merge
num2=`cat num2`
tail -$num2 $Dpath/$merge_path/1/stru_xyz.in_2 | awk -F " " '{print $2"\t"$3"\t"$4}' > coor2

