from urllib.request import urlretrieve


print('''
       |--------------------------------|
       |    DOWNLOAD FILE DEVICE ( 6 )  |
       |--------------------------------|
''')

url_input = input("Enter your file url : ")
output_filename = input("Enter your output file name : ")

urlretrieve(url_input,output_filename)