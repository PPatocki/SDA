#!/bin/bash
touch $1
echo "#include <stdio.h>" >> $1
echo "int main ()" >> $1
echo "{" >> $1
echo '	printf("Hello, '$2'!\n");' >> $1
echo "	return 0;" >> $1
echo "}" >> $1
gcc $1
./a.out
rm $1
rm a.out
