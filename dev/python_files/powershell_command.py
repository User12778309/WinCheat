# powershell -c "Write-Host "second string""

import os

print('''
       |---------------------------------------|
       |    POWERSHELL COMMAND DEVICE ( 4 )    |
       |---------------------------------------|
''')

command_input = input("Enter your command : ")

os.system('powershell -c "' + command_input + '"')