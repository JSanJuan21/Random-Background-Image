import ctypes
from delete import delete_background
from api import download_image

delete_background()
download_image()

def bg():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\jorge.sanjuan\\Pictures\\background.jpg", 0)

bg()