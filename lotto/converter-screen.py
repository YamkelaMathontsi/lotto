# All the imports
from tkinter import *
import requests
from tkinter import messagebox

# Let's start with the design of the GUI
root = Tk()
root.title("Currency Converter")
root.geometry("700x700")
root.config(bg="#5bc0de")

value = IntVar()

# Retrieving the information from an external JSON file as a source of reference
information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']
# print(conversion_rate)


# label results
value_label = Label(root, text="Convert", font=("Serif", 20))
value_label.config(bg="#5bc0de")
value_label.pack()

# entry for the results
value_entry = Entry(root, textvariable=value, width=40)
value_entry.config(bg="orange")
value_entry.pack()

# Creating the FROM (Standard value is USD)
from_label = Label(root, text="From: USD", font=("Serif", 20))
from_label.config(bg="#5bc0de")
from_label.pack()

# Doing the Conversion of the data with its loop
convert = Label(root, text="To:", font=("Serif", 20))
convert.config(bg="#5bc0de")
convert.pack()

convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
    convert_list.config(bg="tan")
    convert_list.pack()

convert_label = Label(root, text="Converted to: ", font=("Serif", 20))
convert_label.config(bg="#5bc0de")
convert_label.pack()


def convert_curr():
    num = float(value_entry.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = ans


convert_btn = Button(root, command=convert_curr, text="Convert", font=("Serif", 20), width=20)
convert_btn.config(bg="pink")
convert_btn.pack()

def clear_text():
    clear_btn.delete(0, END)
    clear_btn.delete(0, END)

def destroy():
    msg_box = messagebox.askquestion("Closing Programing, Are You Sure")
    root.destroy()

clear_btn = Button(root, text='Clear', bg="grey", command=clear_text)
clear_btn.place(x=200, y=420)
exit = Button(root, text='Exit', bg="grey", command=destroy)
exit.place(x=400, y=420)


root.mainloop()
