#! /bin/bash
traj_i=`cat traj_i`
path=`pwd`
Dpath=$path
merge_path=workspace_merge
num1=`cat num1`
num2=`cat num2`

cd $Dpath/$merge_path/$traj_i
mv stru_xyz.in_1 ori_stru1
mv stru_xyz.in_2 ori_stru2
mv vel_xyz.in_1 ori_vel1
mv vel_xyz.in_2 ori_vel2
#echo $num1 > stru_xyz.in_1
#echo ' Geom' >> stru_xyz.in_1
paste $Dpath/sym1 $Dpath/khf_coor_mv.txt >> coordinate.txt
#echo $num1 > vel_xyz.in_1
#echo ' Momenta' >> vel_xyz.in_1
paste $Dpath/sym1 $Dpath/khf_vel_mv.txt >> velocity.txt
#echo $num2 > stru_xyz.in_2
#echo ' Geom' >> stru_xyz.in_2
paste $Dpath/sym2 $Dpath/h2o_coor_center_rotate.txt >> coordinate.txt
#echo $num2 > vel_xyz.in_2
#echo ' Momenta' >> vel_xyz.in_2
paste $Dpath/sym2 $Dpath/h2o_vel_rotate.txt >> velocity.txt
