#!/bin/sh

for i in 0990 0995 1000 1005 1010
do

cat output.relax.$i | grep alat | awk '{print $5}'| head -1 >> data.cell
cat output.relax.$i | grep "total   stress" -A1 | tail -1 |  awk '{print $4}' >> data.c11
cat output.relax.$i | grep "total   stress" -A2 | tail -1 | awk '{print $5}' >> data.c12
cat output.relax.$i | grep "total   stress" -A3 | tail -1 | awk '{print $6}' >> data.c13


done
