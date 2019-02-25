#!/bin/bash
read -p "Podaj silnie do obliczenia: " n

while [[ $n -lt 0 ]]
do
read -p "Podaj silnie do obliczenia: " n
done

i=0
silnia=1

while [[ $i -ne $n ]] 
do
i=$(( $i + 1))
silnia=$(( $silnia*$i ))
done
echo "Silnia z $n rowna sie $silnia"
