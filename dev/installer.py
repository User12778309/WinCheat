import os

if os.path.exists("/WinCheats"):
    if os.path.exists("C:/Program Files/Git/cmd"):
        if os.path.exists("C:/WinCheats/PS2EXE"):
            print("PS2EXE already installed")
        else:
            os.system("cd /WinCheats & git clone https://github.com/MScholtes/PS2EXE.git")
            print("PS2EXE git cloned")
            print("PS2EXE installled")
    else:
        print("Your have not Git : Please install Git")
else:
    os.mkdir("/WinCheats")
    print("Dir created")
    if os.path.exists("C:/Program Files/Git/cmd"):
        if os.path.exists("C:/WinCheats/PS2EXE"):
            print("PS2EXE already installed")
        else:
            os.system("cd /WinCheats & git clone https://github.com/MScholtes/PS2EXE.git")
            print("PS2EXE git cloned")
            print("PS2EXE installled")
    else:
        print("Your have not Git : Please install Git")






