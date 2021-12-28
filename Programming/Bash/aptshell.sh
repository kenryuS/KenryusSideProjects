#!/bin/sh
echo "This is the APT Shell, the shell for APT package manager."
while true
do
	echo -n "(APT Shell)>>> "
	read cmd

	case $cmd in
		update)
			sudo apt update
			echo "These packages are upgradable:"
			sudo apt list --upgradable | less
		;;

		upgrade)
			echo -n "Upgrade the packages? [Y/N]: "
			read yn
			if [ $yn == "Y" ]
				sudo apt upgrade -y
			else
				echo "Upgrade rejected"
			fi
		;;

		install)
			echo -n "Enter the package name: "
			read pkg
			if apt search $pkg
				echo -n "Proccess the installation? [Y/N]: "
				read yn
				if [ $yn == "Y" ]
					sudo apt install $pkg -y
				else
					echo "Installation rejected"
				fi
			else
				echo "error; Pakcage Not Found"
			fi
		;;

		search)
			echo -n "Enter the package name: "
			read pkg
			apt search $pkg | less
		

		remove)
			echo -n "Enter the package name (default=autoremove): "
			read pkg
			if [ -z $pkg ]
				echo -n "Proccess the autoremove? [Y/N]: "
				read yn
				if [ $yn == "Y" ]
					sudo apt autoremove -y
				else
					echo "Autoremove rejected"
				fi
			else
				echo -n "Proccess the removement? [Y/N]: "
				read yn
				if [ $yn == "Y" ]
					sudo apt install $pkg -y
					echo -n "Purge the package? [Y/N]: "
					read yn2
					if [ $yn == "Y" ]
						sudo apt purge $pkg
					else
						echo "Purge rejected"
					fi
	
				else
					echo "removement rejected"
				fi
			fi
		;;

		exit)
			echo "Bye!"
			break

		*)
			echo "error, Command Not Found"
		;;
	esac
	pkg=""
	yn=""
	yn2=""
done
