#! /bin/bash
log_file=473/gmodel51.log
coor_file=473/coor_all
num_sum=`cat num_sum`
num_add=`expr $num_sum + 2`
grep -A $num_add 'Coordinates' $log_file | tail -$num_sum | awk -F " " '{print $4"\t"$5"\t"$6}' >> $coor_file
