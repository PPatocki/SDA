#!/bin/bash
a=$1
b=$2
c=$3
e=-
f=+
g=/
h=*
if [[ $b = $e || $b = $f ]]; then 
let wynik=${a}$b${c}
echo $wynik
elif [[ $b = $g ]]; then
echo $(($a/$c))
elif [[ $b = $h ]]; then
echo $(($a*$c)) 
else
echo "Niedozwolone dzialanie"
fi
