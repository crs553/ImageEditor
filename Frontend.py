from tkinter import *
from Backend import ImgOperations


class MainApp(Frame):
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)

        self.master = master
        self.img = ImgOperations()
        self.imgLab = Label(self, text="Hello")
        self.imgLab.place(x=0,y=0)

        self.init_window()

    def init_window(self) -> None:
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        # menu_bar = MenuBar(self.master)
        # self.master.config(menu=menu_bar)
        menu = Menu(self.master, tearoff=0)  # , tearoff=False)
        self.master.config(menu=menu)

        """File Menu Tab"""
        file = Menu(menu)
        file.add_command(label="Exit", underline=1, command=self.clse)
        file.add_command(label='Open', underline=1, command=self.open_File)
        menu.add_cascade(label="File", underline=0, menu=file)

        """Edit Menu Tab"""
        edit = Menu(menu)
        edit.add_command(label="Undo", underline=1, command=self.img.reverse)


    def open_File(self):
        filename = self.img.getImgLink()
        self.img.setImage(filename)
        self.imgLab.destroy()
        self.imgLab = Label(self, image=self.img.getImage())
        self.imgLab.image = self.img.getImage()
        self.imgLab.place(x=0, y=0)

    def clse(self) -> None:
        exit()

    def undo(self) -> None:
        """
        Function for reversing image changes
        """
        pass


def main():
    root = Tk()
    root.geometry("900x900")
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
