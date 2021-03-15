#! /bin/sh

l=$((1))
clear

while [ $l != 0 ]
do
	clear
	echo "What mode would you like to do:"
	echo "1: search, 2: install, 3: uninstall, 4: list installed packages, 5: list the repository, 6: package update, 7: distro upgrade"
	read m

	if [ $m = "1" ]
	then
		echo "This will search the package"
		echo "Package name:"
		read pkgn
		apt search $pkgn
		read stop
	elif [ $m = "2" ]
	then
		echo "This will install the package"
		echo "Package name:"
		read pkgn
		sudo apt install $pkgn
		read stop
	elif [ $m = "3" ]
	then
		echo "This will remove the package"
		echo "Package name:"
		read pkgn
		sudo apt remove $pkgn
		read stop
	elif [ $m = "4" ]
	then
		echo "This will show the list of installed package"
		apt list --installed
		read stop
	elif [ $m = "5" ]
	then
		echo "This will show the package list in the system local repository"
		apt list
		read stop
	elif [ $m = "6" ]
	then
		echo "This will update the packages"
		sudo apt update
		clear
		sudo apt list --upgradable
		echo "Upgrade?[Y/n]:"
		read y
		if [ $y = "Y" ]
		then
			sleep 3
			sudo apt upgrade
		else
			break
		fi
	fi

	clear
	echo "continue?[press 1 to cont. or press 0 to break]"
	read li
	l=$(($li))	
done
