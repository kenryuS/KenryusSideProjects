#! /bin/sh

x=1
echo "This program is the git controller with much more userfriendly"

while [ $x = "1" ]
do
cd /home/kenryu/Git
ls
echo "Which git repository do you want to control?"
read repo
cd $repo
git status
echo "what control do you want to perform?"
echo "commit, pull, push, add"
read ope
if [ $ope = "commit" ]
then
echo "type the message of this commit."
read message
git commit -m "$message"
read stopper
elif [ $ope = "add" ]
then
echo "This operation add the file to commit."
git add .
read stopper
elif [ $ope = "pull" ]
then
git pull
read stopper
elif [ $ope = "push" ]
then
git push
read stopper
fi
clear
done
