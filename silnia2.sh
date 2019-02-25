#!/bin/bash
s=0
silnia=1
read -p "Podaj liczbe " s
for ((i=1; i <= $s ; i++))
do
silnia=$(( $silnia*$i))
done
echo "$silnia"
