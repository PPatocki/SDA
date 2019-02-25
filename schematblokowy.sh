#!/bin/bash
read -p "Czy lampa dziala?(Yes/No)" work
if [[ $work = Yes || $work = yes ]]; then
echo "Skoro dziala to nie ma problemu. Naraaa"
elif [[ $work = No || $work = no ]]; then
read -p "Czy lampa jest podpieta do pradu?(Yes/No)" prad
	if [[ $prad = Yes || $prad = yes ]]; then
		read -p "Czy zarowka jest spalona? (Yes/No)" zarowka
			if [[ $zarowka = Yes || $zarowka = yes ]]; then
			echo " Wymien zarowke."
			elif [[ $zarowka = No || $zarowka = no ]]; then
			echo "Kup nowa lampe"
			fi
	elif [[ $prad = No || $prad = no ]]; then
	echo "Podlacz lampe do pradu."
	fi
fi
