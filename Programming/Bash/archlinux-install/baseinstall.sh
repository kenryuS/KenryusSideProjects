echo "This program will start the installation of the arch linux."
echo -n "Start the process?: [Y/N] "; read yn1
if [[ $yn1 == "N" ]]; then
    echo "exited"
else; then
    pass
fi
echo "Backuping the mirrorlist..."
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup
echo "update mirrorlist by download speed..."
reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist
echo -n "Start the installation of base system?: [Y/N] "; read yn1
if [[ yn1 == "Y" ]]; then
    pacstrap /mnt/ base linux linux-firmware net-tools networkmanager openssh vi mc htop nano neofetch timeshift
    genfstab -U /mnt >> /mnt/etc/fstab
    echo "Verifiying the fstab..."
    if cat /mnt/ect/fstab; then
        echo "Verified!"
    else
        echo "Failed, exit the program with CTRL + C!"
        read
else
    echo "Exit the program with CTRL + C!"
    read
fi