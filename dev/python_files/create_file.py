import os

def mkfile(file_name):
    with open(file_name,"w+") as file:
        file.close()

def mkdir(folder_name):
    try:
        os.mkdir(folder_name)
    except FileNotFoundError:
        pass


print('''
       |--------------------------------|
       |    CREATE FILE DEVICE ( 1 )    |
       |--------------------------------|
''')
path_input = input("Enter target path : ")

print('''
1 ) File
2 ) Folder
3 ) List of file 
4 ) List of folder
''')
device1_num_choice = int(input("Enter your device number : "))

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

if device1_num_choice == 1:
    file_output_path = input("Enter your file path : ")
    mkfile(file_output_path)

elif device1_num_choice == 2:
    folder_output_path = input("Enter your folder path : ")
    mkdir(folder_output_path)

elif device1_num_choice == 3:
    file_path_List = input("Enter your file list path : ")
    with open(file_path_List,"r+") as file_list_file:
        all_file_path_list = file_list_file.read().split("\n")
        for file in all_file_path_list:
            mkfile(file)

elif device1_num_choice == 4:
    folder_path_List = input("Enter your folder list : ")
    with open(folder_path_List,"r+") as folder_list_file:
        all_folder_path_list = folder_list_file.read().split("\n")
        for folder in all_folder_path_list:
            mkdir(folder)