#! /bin/bash
for ((i=1;i<=500;i++))
do
    cp -r ${i}/tmp ${i}_tmp
    cp constant.py ${i}_tmp
    cp matrix_reaction.py ${i}_tmp
    echo ${i}_tmp >> Matrix_reaction
    cd ${i}_tmp
    python3 matrix_reaction.py 
    cd ..
done
