#! /bin/sh

i="1"
while [i -lt 11]
do
echo "Hello Bash! " + $i
i=$[$i+1]
done