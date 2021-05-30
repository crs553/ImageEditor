

from tkinter import *
import Backend
from tkinter.filedialog import askopenfile

image = None

def firstWindow(self):
    win = tK.Tk()
    frame = Frame(win, width=1000, height=500)
    frame.pack(fill=None, expand=False)
    win.title("Image Editor - Open File")

    # button.pack(pady=50)
    win.mainloop()


class OpenWindow:
    def __init__(self, master):
        self.master = master
        master.title("Open Image File")

        self.button = Button(master, text="Open File", command=lambda: self.openImgSeq())
        self.button.pack(pady=300, padx=300)

    def openImgSeq(self):
        imgPath = Backend.getImgLink()
        img = Backend.openImage(imgPath)
        global image
        image = img
        self.close()

    def close(self):
        self.master.destroy()


class ImageDisplay:
    def __init__(self, master, img):
        canvas = Canvas(master, width = 1920, height = 1080)
        canvas.Canvas.pack()
        img = PhotoImage(file = img)

# class
#
def main():
    global image
    image = None
    root = Tk()
    gui = OpenWindow(root)
    print(image)
    root.destroy()
    root.mainloop()


if __name__ == "__main__":
    main()
