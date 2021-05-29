import PIL.JpegImagePlugin
import numpy as np
import PIL as p
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import Optional
from PIL import Image


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class ImgOperations:
    def __init__(self) -> None:
        self.imgPath = self.getImgLink()
        self.image = self.openImage("/home/charles/Documents/Wallpaper/2106257.png")


    def getImgLink(self) -> Optional[str]:
        Tk().withdraw()
        filename = askopenfilename()
        if filename is None:
            return None
        return filename


    def openImage(self,filename: str):
        with Image.open(filename) as im:
            print(filename)
            im.show()
            return im


    def getRed(im_data):
        imRed = np.zeros(im_data.shape, dtype='unit8')
        imRed[:, :, 0] = im_data[:, :, 0]
        return Image.fromarray(imRed)


    def getGreen(im_data):
        imGreen = np.zeros(im_data, dtype='uint8')
        imGreen = im_data[:, :, 1]
        return Image.fromarray(imGreen)


    def getBlue(im_data):
        imBlue = np.zeros(im_data, dtype='uint8')
        imBlue = im_data[:, :, 2]
        return Image.fromarray(imBlue)
    
    def getImage(self):
        return self.image


def main():
    program = False
    # while exit is False:
    # filename = getImgLink() uncomment LATER
    im = ImgOperations()
    im_data = np.array(im)
    print(im_data.shape)


if __name__ == '__main__':
    main()