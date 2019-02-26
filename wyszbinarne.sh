#!/bin/bash
arr=(2 4 6 8 10 12 14 16)
read -p "Wyswietl indeks liczy: " y

#prawa=${arr[${#arr[@]}-1]}
#lewa=${arr[0]}

lewa=0
prawa=$(( ${#arr[@]}-1))

while [[ $lewa -lt $prawa ]]
	do
	srodek=$((( $lewa+$prawa)/2))
		if [[ ${arr[$srodek]} -lt $y ]]; then
			lewa=$(( $srodek+1 ))
		else
			prawa=$srodek
		fi
	done
if [[ ${arr[$lewa]} -eq $y ]]; then
indeks=$lewa
else
indeks=brak
fi
echo "$indeks"
#indeksowane od 0 w n elementowej tablicy
