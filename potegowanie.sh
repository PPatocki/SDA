#!/bin/bash
wynik=1
read -p "Podaj liczbe ktora chcesz potegowac: " a
read -p "Podaj potege do ktorej chcesz podniesc liczbe: " b
while [[ $b -gt 0 ]]
do
wynik=$(( $wynik*$a))
b=$(( $b-1))
done
echo "$wynik"

