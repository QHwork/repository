#! /bin/bash
path=`pwd`
Dpath=$path
merge_path=workspace_merge
traj_i=`cat traj_i`
num2=`cat num2`
tail -$num2 $Dpath/$merge_path/$traj_i/stru_xyz.in_2 | awk -F " " '{print $2"\t"$3"\t"$4}' > h2o_coor.txt
