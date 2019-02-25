#!/bin/bash
i=0
while [ $i -lt 10 ]
do
	touch pliknumer$i
	i=$((i+1))
done
