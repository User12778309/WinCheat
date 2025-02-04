import getpass
import platform
import socket

print('''
       |-----------------------------------------|
       |    GET INFO DEVICE ( 11 )               |
       |-----------------------------------------|

''')

print("User name -----------> " + getpass.getuser())
print("Platform ------------> " + platform.system())
print("IP ------------------> " + socket.gethostbyname(socket.gethostname()))
print("Host name -----------> " + socket.gethostname())