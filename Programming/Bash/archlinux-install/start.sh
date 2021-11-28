echo "This bash script will check the internet connection, partitioning the disk, formating the partition, and mount the partitions to install Arch Linux."
echo -n "Start the process?: [Y/N] "; read yn1
if [[ $yn1 == "N" ]]; then
    echo "exited"
else
    pass
fi
echo "Checking internet connection..."
if ping -c 3 google.com; then
    echo "Internet connection verified."
else
    echo "Internet connection has not verified, the additional configuration starts."
    ip a
    echo -n "Select the Network Interface: "; read netint
    echo -n "Set the IP address: "; read ipadd
    echo -n "Set the GateWay IP address"; read gwip
    echo -n "Set the Netmask: "; read netmk
    ip addr flush dev $netint
    ifconfig $netint $ipadd netmask $netmk
    route add default gw $gwip
    echo "nameserver $gwip" >> /etc/resolv.conf
    echo "nameserver 8.8.8.8" >> /etc/resolv.conf
fi
echo -n "Partitioning the Disk automatically?: [Y/N] "; read yn2
if [[ yn2 == "N" ]]; then
    fdisk -l
    echo -n "Select the drive to manipulate: "; read disk
    fdisk $disk
    echo -n "Hit Enter to go into sub shell to format the disk partition: "; read
    bash
elif [[ yn2 == "Y" ]]; then
    fdisk -l
    echo -n "Select the drive to manipulate: "; read disk
