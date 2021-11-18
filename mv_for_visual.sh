#! /bin/bash
path=`pwd`
Dpath=$path
merge_path=workspace_merge
num1=`cat num1`
tail -$num1 $Dpath/$merge_path/1/stru_xyz.in_1 | awk -F " " '{print $2"\t"$3"\t"$4}' > khf_coor.txt

