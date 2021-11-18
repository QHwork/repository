#!/bin/bash
#files=$*
files=`cat for_run`
prog="rung16 -q eth"
maxjob=20
rjobs=0
for f in $files ; do
  while [ "$maxjob" -le "$rjobs" ] ; do
    sleep 5
    line=`jst | awk '{print $5}' | grep 'Q' | wc -l`
    lines=`jst | awk '{print $5}' | grep 'R' | wc -l`
    rjobs=$((line + lines))
  done
  $prog $f
  rjobs=$((rjobs+1))
done
