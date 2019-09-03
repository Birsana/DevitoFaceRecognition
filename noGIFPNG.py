#I used the fatkun chrome extension to download pictures off google images for my classifier.
#However, some are in the format of .gif or .png, which can't be used.
#Here I delete the .gif files and convert the .png files to .jpg

import os
import os.path

path = "/Users/andreb/Desktop/classifier/devito"

pictures = os.listdir(path)

for picture in pictures:
    if picture.endswith(".gif"):
        os.remove(os.path.join(path, picture))
    elif picture.endswith(".png"):
        newPic = picture.replace('.png', '.jpg')
        os.rename(os.path.join(path, picture),
                 os.path.join(path,newPic))