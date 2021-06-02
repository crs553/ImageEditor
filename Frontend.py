import tkinter
from tkinter import *
import Backend
from tkinter.filedialog import askopenfile
from functools import partial

root = Tk()
root.title("Open Image")
root.geometry("200x300")

back_Img = None
top = None
photo = None



def openImg():
    global back_Img
    back_Img = Backend.ImgOperations()
    top = Toplevel()
    btn = Button(top, text="Hello")
    top.mainloop()

open_btn = Button(root, text="Open Image", command=lambda: openImg())
open_btn.grid(row=0, column=0)



root.mainloop()

# if __name__ == "__main__":
#     main()
