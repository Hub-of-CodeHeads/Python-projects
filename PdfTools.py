from tkinter import *
import PyPDF2

if __name__ == "__main__":
    root = Tk()
    root.configure(background='light blue')
    root.title("test image app")
    root.geometry("400x400")

    frame = Frame(root, width=350, height=300, background="navy blue")
    frame.pack()
    frame.place(anchor='center', relax=0.5, rely=0.5)

    root.mainloop()