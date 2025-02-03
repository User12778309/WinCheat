import os

print('''
       |--------------------------------|
       |    SHUTDOWN PC DEVICE ( 3 )    |
       |--------------------------------|
''')

choose_input = input("Would you shutdown pc (y/n) : ")

if choose_input == "y":
    os.system("shutdown /s")

else:
    pass