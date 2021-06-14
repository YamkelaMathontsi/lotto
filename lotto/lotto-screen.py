from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("images")
root.geometry("500x500")
photo = PhotoImage(file="ITHUBA-NATIONAL-LOTTERY.png")
pic_label = Label(root, image=photo)
pic_label.place(x=20, y=10)

#Label and entry
name = Label(root, text="Name:")
name.place(x=20, y=150)
name_ent = Entry(root, text="")
name_ent.place(x=20, y=170)

#Label and entry
code = Label(root, text="Code:")
code.place(x=200, y=150)
code_ent = Entry(root, text="")
code_ent.place(x=200, y=170)


ticket_spinbox = Spinbox(root, width=5, from_=0, to=49)
ticket_spinbox.place(x=320, y=200)
ticket_spinbox = Spinbox(root, width=5, from_=0, to=49)
ticket_spinbox.place(x=260, y=200)
ticket_spinbox = Spinbox(root, width=5, from_=0, to=49)
ticket_spinbox.place(x=200, y=200)
ticket_spinbox = Spinbox(root, width=5, from_=0, to=49)
ticket_spinbox.place(x=140, y=200)
ticket_spinbox = Spinbox(root, width=5, from_=0, to=49)
ticket_spinbox.place(x=80, y=200)
ticket_spinbox = Spinbox(root, width=5, from_=0, to=49)
ticket_spinbox.place(x=20, y=200)





root.mainloop()
