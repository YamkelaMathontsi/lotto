from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("images")
root.geometry("500x500")
photo = PhotoImage(file="bottom img.png")
pic_label = Label(root, image=photo)
pic_label.place(x=10, y=10)
# photo_2 = PhotoImage(file="lott.jpg")
# pic2_label = Label(root, image=photo_2)
# pic2_label.place(x=20, y=100)

def clear_text():
    name.delete(0, END)
    email.delete(0, END)

def destroy():
    msg_box = messagebox.askquestion("Closing Programing, Are You Sure")
    root.destroy()


# Labels

name = Label(root, text="Name:")
name.place(x=20, y=250)
email = Label(root, text="Email Address:")
email.place(x=20, y=300)
id_num = Label(root, text="ID Number")
id_num.place(x=20, y=350)

#Entries

name = Entry(root, text="")
name.place(x=130, y=250)
email = Entry(root, text="")
email.place(x=130, y=300)
id_num = Entry(root, text="")
id_num.place(x=130, y=350)


def user_pass_search():

    user_pass = {'Jayden': 'jaydenmay', 'Brent Lee': 'yourstepbro', 'Jason': 'faketaxi@17',
             'Yamkela': '@merclife'}

    if name.get() in user_pass:
        if email.get() == user_pass[name.get()]:
            root.destroy()
            # import newwindow
        else:
            messagebox.showerror(message="Username and password does not match")
    else:
        messagebox.showerror(message="Username does not exist")

verify = Button(root, text='Verify', bg="pink", command=user_pass_search )
verify.place(x=20, y=400)
clear_btn = Button(root, text='Clear', bg="pink", command=clear_text)
clear_btn.place(x=120, y=400)
exit = Button(root, text='Exit', bg="pink", command=destroy)
exit.place(x=220, y=400)


root.mainloop()

