#!/bin/bash
numbers=(1 2 3 4 5 6 7 8)
arithmetic=$(( ${numbers[0]} + ${numbers[${#numbers[@]}-1]} * ${#numbers[@]} / 2 ));
echo $arithmetic
# niedziala bo bash dziala na integerach
