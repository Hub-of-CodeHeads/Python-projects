from tkinter import *
import PyPDF2
from tkinter import filedialog
from tkinter.filedialog import askopenfile


def upload_file():
    f_types = [('Pdf files', '*.pdf')]
    filename = filedialog.askopenfilename(filetypes=f_types)


if __name__ == "__main__":
    root = Tk()
    root.configure(background='navy blue')
    root.title("PDF Tools App")
    root.geometry("400x400")

    frame = Frame(root, width=350, height=300, background="light blue")
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    heading = Label(frame, text="PDF Tools", font=('Helvatical bold', 20), bg="light blue")
    btn1 = Button(frame, text="Merge PDF", font=('Halvetical bold', 15), height=1, width=12, bg="Light green", command=lambda: upload_file())
    btn2 = Button(frame, text="Add Pages", font=('Halvetical bold', 15), height=1, width=12, bg="Light green")
    btn3 = Button(frame, text="Delete Pages", font=('Halvetical bold', 15), height=1, width=12, bg="Light green")
    btn4 = Button(frame, text="Separate Pages", font=('Halvetical bold', 15), height=1, width=12, bg="Light green")

    heading.place(anchor='center', relx=0.5, rely=0.20)
    btn1.place(anchor='center', relx=0.28, rely=0.60)
    btn2.place(anchor='center', relx=0.72, rely=0.60)
    btn3.place(anchor='center', relx=0.28, rely=0.80)
    btn4.place(anchor='center', relx=0.72, rely=0.80)

    root.mainloop()
