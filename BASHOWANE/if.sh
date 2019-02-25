#!/bin/bash
read -p "Jaki masz kolor wlosow:" kolor


if [[ $kolor = "blad" ]]; then
	echo "Siema blondi"
elif [[ $kolor = "czarny" ]]; then
	echo "Oczyyyy czornyjeee"
elif [[ $kolor = "rudy" ]]; then
	echo "rudy rudy rudy rydz"
else 
	echo "A spierrrrr"
fi
