#!/bin/sh

grep CELL_PARAMETERS output.out | awk '{print $3}'
X=$(echo "scale=10; $i*2.45/1000" | bc);
