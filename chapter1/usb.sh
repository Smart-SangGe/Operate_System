#!/bin/bash

start_menu() {
    echo "1) Mount USB drive"
    echo "2) Unmount USB drive"
    echo "3) Show USB drive info"
    echo "4) Copy files to USB drive"
    echo "5) Copy files to local drive"
    echo "6) Exit" 
    echo "Enter your choice:"
}

while true; do
    # Display menu
    start_menu

    # Read user input
    read choice

    # Execute option based on choice
    case $choice in
        1)
            echo "Scanning usb"
            # auto mount all usb drive
            # Loop through all available drives and mount them
            for dev in $(lsblk -ln -o NAME,TRAN | grep 'usb' | awk '{print $1}'); do
                if [[ -e "$dev" ]]; then
                    # Use udisks2 to mount the device
                    udisksctl mount -b $dev
                fi
            done
			echo "All usb drive mounted"
            ;;
        2)
            echo "Scanning usb"
            # auto unmount all usb drive
            # Loop through all mounted drives and unmount them
            for dev in $(lsblk -ln -o NAME,MOUNTPOINT,TRAN | grep 'usb' | awk '$2 {print $1}'); do
            # Check if the device is mounted
                if mount | grep -q "$dev"; then
                    # Use udisks2 to unmount the device
                    udisksctl unmount -b $dev
                fi
            done
			echo "All usb drive unmounted"
            ;;
        3)
            echo "All usb info"
            # show all usb info
            # Display information about all USB devices
			lsusb
            ;;
        4)
            echo "input 'source' 'destination'"
            # copy file from local to usb drived
            # Check if the source file exists
            if [ ! -f "$source" ]; then
                echo "Source file does not exist!"
                exit 1
            fi

            # Check if the destination directory exists
            if [ ! -d "$destination" ]; then
                echo "Destination directory does not exist!"
                exit 1
            fi

            # Copy the file
            cp "$source" "$destination"
            echo "File copied successfully."
            ;;
        5)
            echo "input 'source' 'destination'"
            # copy file from usb drive to local
            # Read the source and destination from the user
            read source destination

            # Check if the source file exists (assuming it's from the USB drive)
            if [ ! -f "$source" ]; then
                echo "Source file does not exist on the USB drive!"
                exit 1
            fi
            # Check if the destination directory exists
            if [ ! -d "$destination" ]; then
                echo "Destination directory does not exist on local storage!"
                exit 1
            fi

            # Copy the file from USB drive to local directory
            cp "$source" "$destination"
            echo "File copied successfully from USB to local storage."
            ;;
        6)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice! Please select a valid option."
            ;;
    esac
done