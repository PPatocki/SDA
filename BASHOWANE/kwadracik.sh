#!/bin/bash
kwadracik() {
a=$1
b=$a
for ((i=0; i<a; i++))
do
	echo -n "*"
	echo -e "*\c"	
done
}	 
kwadracik $1


