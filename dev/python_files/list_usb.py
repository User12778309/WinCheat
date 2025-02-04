import psutil


print('''
       |--------------------------------|
       |    LIST USB DEVICE ( 7 )       |
       |--------------------------------|
''')

def list_usb_devices():
    # Get all disk partitions
    partitions = psutil.disk_partitions(all=False)

    usb_devices = []

    for partition in partitions:
        # Check if the device is a USB device
        if 'removable' in partition.opts:
            usb_info = {
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'fstype': partition.fstype,
                'opts': partition.opts
            }
            usb_devices.append(usb_info)

    return usb_devices


def main():
    usb_devices = list_usb_devices()

    if usb_devices:
        print("USB Devices Found:")
        for device in usb_devices:
            print(f"Device: {device['device']}")
            print(f"  Mount Point: {device['mountpoint']}")
            print(f"  File System Type: {device['fstype']}")
            print(f"  Options: {device['opts']}")
            print()
    else:
        print("No USB devices found.")

main()