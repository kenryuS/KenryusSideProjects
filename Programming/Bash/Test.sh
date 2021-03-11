#! /bin/sh

i=$((1))
while [ $i = 10 ]
do
echo "Hello Bash! " + $i
i=$(( $i + 1))
sleep 1
done