from typing import Optional
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import numpy as np


class ImgOperations:
    def __init__(self) -> None:
        """
        Gets image from an askfilename dialogue
        """
        self.stack = []
        self.imgPath = None
        self.image = None
        self.original = None
        self.raw = None

    """Image Opening and Changing"""

    def getImgLink(self) -> Optional[str]:
        # Tk().withdraw()
        filename = askopenfilename()
        return filename

    def setImage(self, filename: str):
        self.raw = Image.open(filename)
        self.image = ImageTk.PhotoImage(self.raw)
        self.setPath(filename)
        self.setOriginal()
        self.__addStack(self.image)

    def __addStack(self, val) -> None:
        self.stack.append(val)

    def resetStack(self):
        self.stack = []

    def popStack(self):
        return self.stack.pop()

    def getPath(self):
        return self.imgPath

    def getImage(self):
        return self.image

    def setPath(self, filename: str):
        self.imgPath = filename

    def setOriginal(self):
        self.original = self.stack[0]

    def getOriginal(self):
        return self.original

    def reverse(self):
        pass

    def reverseToOrigin(self):
        self.image = self.original

    """Image Manipulations"""

    def getRed(self,im_data):
        imRed = np.zeros(im_data.shape, dtype='unit8')
        imRed[:, :, 0] = im_data[:, :, 0]
        self.image = Image.fromarray(imRed)
        self.__addStack(self.image)

    def getGreen(self,im_data):
        imGreen = np.zeros(im_data, dtype='uint8')
        imGreen = im_data[:, :, 1]
        self.image = Image.fromarray(imGreen)
        self.__addStack(self.image)

    def getBlue(self,im_data):
        imBlue = np.zeros(im_data, dtype='uint8')
        imBlue = im_data[:, :, 2]
        self.image =  Image.fromarray(imBlue)
        self.__addStack(self.image)
