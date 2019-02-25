#!/bin/bash

min=100
for i in $@
do
	if [[ $i -lt $min ]]; then
	min=$i
	fi
done
echo $min
