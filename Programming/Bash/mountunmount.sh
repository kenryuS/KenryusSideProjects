#! /bin/sh

clear
echo "This shell file mount/unmount the removable hard drive."
cd /media/kenryu/
echo "mount(1) or unmount(2) the drive?"
read mode

if [ $mode -eq 1 ]
then
sudo fdisk -l
echo "select hard drive(ex. sda1):"
read ehh
ls
echo "select mount point(ex. /media/kenryu/SD1):"
read mp
clear
echo "loading..."
sleep 3
sudo mount $ehh $mp
echo "mounting /dev/$ehh to $mp ..."
sleep 1.5
elif [ $mode -eq 2 ]
then
ls
echo "Select the dive to unmount(ex. usb128):"
read mp
clear
echo "loading..."
sleep 3
sudo umount /media/kenryu/$mp
echo "unmounting $mp ..."
sleep 1.5
fi
echo done
read io
