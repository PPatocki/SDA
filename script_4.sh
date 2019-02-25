#!/bin/bash


num=$( cat $1 )
suma=0
for i in $num
do 
	suma=$(( $suma + $i ))
	echo $suma
done
echo "Suma wszystkich cyfr w pliku: $suma"	
