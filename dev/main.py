print('''
                ------------------------------------------------------------------------------
                | 1 : Create file                    | 7 : Get ip/user/machine name          |
                | 2 : Remove file                    | 8 : Compile Powershell                |
                | 3 : Cmd command                    | 9 : Open Webcam                       |
                | 4 : Powershell command             | 10 : Shutdown                         |
                | 5 : Open URL                       | 11 : Change background                |              
                | 6 : Download file ( URL )          | 12 : List USB ( Windows )             |              
                |-----------------------------------------------------------------------------
''')
while True:
    print("\n")
    device_num_input = int(input("[Your device ( num ) ]> "))
    print("\n")

    if device_num_input == 1:
        import python_files.create_file

    if device_num_input == 2:
        import python_files.remove_file

    if device_num_input == 3:
        import python_files.cmd_command

    if device_num_input == 4:
        import python_files.powershell_command

    if device_num_input == 5:
        import python_files.open_url

    if device_num_input == 6:
        import python_files.download_file

    if device_num_input == 16:
        import python_files.list_usb

    if device_num_input == 15:
        import python_files.change_bg

    if device_num_input == 14:
        import python_files.shutdown_pc

    if device_num_input == 13:
        import python_files.open_webcam

    if device_num_input == 11:
        import python_files.get_user_info

    if device_num_input == 12:
        import python_files.compile_powershell
