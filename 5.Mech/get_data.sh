#!/bin/sh

for i in 0990 0995 1000 1005 1010
do

cat output.$i | grep CELL_ -A1 | sed '1~d' | awk '{print $1}' >> data.cell
cat output.$i | grep "total   stress" -A1 | sed '1~d' | awk '{print $4}' >> data.c11
cat output.$i | grep "total   stress" -A2 | sed '1~d' | sed '1~d' | awk '{print $5}' >> data.c12
cat output.$i | grep "total   stress" -A3 | tail -1 | awk '{print $6}' >> data.c13


done
