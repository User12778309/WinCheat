print('''
                ------------------------------------------------------------------------------
                | 1 : Create file                    | 11 : Get ip/user/machine name         |
                | 2 : Remove file                    | 12 : Open file                        |
                | 3 : Cmd command                    | 13 : Open directory                   |
                | 4 : Powershell command             | 14 : Write JS file ( HTML )           |
                | 5 : Open URL                       | 15 : Create HTML page                 |
                | 6 : Download file ( URL )          | 16 : Inject python                    |
                | 7 : List USB ( Windows )           | 17 : Crypt text                       |
                | 8 : Change background              | 18 : Decrypt text                     |
                | 9 : Shutdown                       | 19 : Check python                     |
                | 10 : Open Webcam / Another device  | 20 : Read File                        |
                |                        20 : Compile Powershell                             |
                ------------------------------------------------------------------------------
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

    if device_num_input == 7:
        import python_files.list_usb

    if device_num_input == 8:
        import python_files.change_bg

    if device_num_input == 9:
        import python_files.shutdown_pc
