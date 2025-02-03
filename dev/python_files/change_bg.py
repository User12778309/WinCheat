import ctypes

print('''
       |-----------------------------------------|
       |    CHANGE BACKGROUND DEVICE ( 8 )       |
       |-----------------------------------------|
''')

wallpaper_path_input = input("Enter your wallpaper path : ")

image = ctypes.c_wchar_p(wallpaper_path_input)
ctypes.windll.user32.SystemParametersInfoW(20,0,image,0)