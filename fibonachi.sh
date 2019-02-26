#!/bin/bash
read -p "Podaj liczbe elementow ciagu fibonachiego do wyswietlenia: " f

f0=0
f1=1
echo -n "$f0 $f1"
for (( i=2; i <= $f; i++ ));
	do
	tmp=$f1
	f1=$(( $f0+$f1))
	f0=$tmp
	echo -n " $f1"
	done
echo ""

