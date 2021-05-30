import tkinter
from tkinter import *
import Backend
from tkinter.filedialog import askopenfile


class ImgWindow:
    def __init__(self, master : tkinter.Tk):
        self.master = master
        imgPath = Backend.getImgLink()
        if imgPath == ():
            raise FileNotFoundError
        win = Toplevel(master)
        win.geometry(1920,1080)
        img = Backend.openImage(imgPath)
        canvas = Canvas(master)
        canvas.pack()
        canvas.create_image(10,10,iamge = imgPath,anchor = NW)



    def openImgSeq(self):
        imgPath = Backend.getImgLink()
        print(imgPath)
        if imgPath == ():
            pass
        else:
            self.button.destroy()
            img = Backend.openImage(imgPath)
            canvas = Canvas(self.master, bg='black')
            canvas.pack(expand=YES, fill=BOTH)
            canvas.create_image(20, 20, image=img, anchor=NW)
            self.master.update()

    def dispImg(self):
        pass

    def close(self):
        self.master.destroy()


def main():
    root = Tk()
    root.title("Image Editor")
    button = Button(root, text="Open File", command=lambda: ImgWindow(root))
    button.pack(pady=300, padx=300)
    root.mainloop()


if __name__ == "__main__":
    main()
