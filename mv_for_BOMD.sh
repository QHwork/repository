#! /bin/bash
traj_i=`cat traj_i`
num1=`cat num1`
path=`pwd`
Dpath=$path
merge_path=workspace_merge
tail -$num1 $Dpath/$merge_path/$traj_i/stru_xyz.in_1 | awk -F " " '{print $2"\t"$3"\t"$4}' > khf_coor.txt
tail -$num1 $Dpath/$merge_path/$traj_i/vel_xyz.in_1 | awk -F " " '{print $2"\t"$3"\t"$4}' > khf_vel.txt
