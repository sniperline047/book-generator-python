#fork this repo
#paste is in a New FOlder on Desktop
#copy your book there
#run "python ./bookGenerate.py"
#Awesome! Your book is generated
#Now just select all file and print

import pyautogui
import os
import time
from PIL import Image
from tqdm import tqdm


# PARAMETERS
left = 620 #specify_your_dimensions
right = 1920 - 620 #specify_your_dimensions
top = 100 #specify_your_dimensions
bottom = 1080 - 100 #specify_your_dimensions
base = "C:/Users/your_user_name/Desktop/New folder/" #change here
bookName = "MyBook.acsm" # .acsm --> adobe digital edition extension
end = 765 #no of pages in book

def main():
    print("Opening file [1/3]\n")
    try:
        fileLoc = "base%s" % (bookName)
        os.startfile(fileLoc)
        time.sleep(5) #time to waste for downloading book
        pyautogui.click(500, 500) #click to active this tab
        takeScreen()
    except Exception, e:
        print(e)

def takeScreen():
    print("Starting capture [2/3]\n")
    for i in tqdm(range(1, end + 1)):
        newAdd = "%sname%s.png" % (base, i)
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(newAdd)
        pyautogui.typewrite(['down'])
        time.sleep(1)

    print("Cropping ... [3/3]\n")

    for i in tqdm(range(1, end + 1)):
        newAdd = "%sBook/photo%s.png" % (base, i)
        im = Image.open(newAdd)
        im1 = im.crop((left, top, right, bottom))
        name = "photo%s.png" % (i)
        im1.save(name)
    
    print("Finish!")

main()

