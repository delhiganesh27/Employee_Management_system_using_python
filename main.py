from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Employee management system")
root.geometry("1200x700+0+0")  # 0+0 denotes starts at (0,0)
root.config(bg="#2c3e50")
root.state("zoomed")

# variables
name = StringVar()
gender = StringVar()
age = StringVar()
doj = StringVar()
email = StringVar()
contact = StringVar()
address = StringVar()

# entries frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="employee management system",
              font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20)

# Name
lblName = Label(entries_frame, text="Name", font=(
    'Calibri', 16), bg="#535c68", fg="white")
# sticky for left alignment  w-west(left) e-east
lblName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
txtName = Entry(entries_frame, textvariable=name,
                font=('Calibri', 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10)

# Age
lblAge = Label(entries_frame, text="Age", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky='w')
txtAge = Entry(entries_frame, textvariable=age, font=('Calibri', 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10)

# Gender
lblGender = Label(entries_frame, text="Gender", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblGender.grid(row=2, column=0, padx=10, pady=10, sticky='w')
# for combo box use ttk class from tkinter
# state is for prevent typing which allows only selection
comboGenders = ttk.Combobox(entries_frame, font=(
    'Calibri', 16), width=28, textvariable=gender, state="readonly")
comboGenders['values'] = ('Male', 'Female')
# txtGender = Entry(entries_frame, textvariable=gender,
#                   font=('Calibri', 16), width=30)
comboGenders.grid(row=2, column=1, padx=10, pady=10)

# Date of join
lblDoj = Label(entries_frame, text="Doj", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblDoj.grid(row=2, column=2, padx=10, pady=10, sticky='w')
txtDoj = Entry(entries_frame, textvariable=doj, font=('Calibri', 16), width=30)
txtDoj.grid(row=2, column=3, padx=10, pady=10)

# Email
lblEmail = Label(entries_frame, text="Email", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblEmail.grid(row=3, column=0, padx=10, pady=10, sticky='w')
txtEmail = Entry(entries_frame, textvariable=email,
                 font=('Calibri', 16), width=30)
txtEmail.grid(row=3, column=1, padx=10, pady=10)

# Contact
lblContact = Label(entries_frame, text="Contact", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky='w')
txtContact = Entry(entries_frame, textvariable=contact,
                   font=('Calibri', 16), width=30)
txtContact.grid(row=3, column=3, padx=10, pady=10)


# Address
lblAddress = Label(entries_frame, text="Address", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky='w')
txtAddress = Text(entries_frame,
                  font=('Calibri', 16), width=85, height=5)
txtAddress.grid(row=5, column=0, padx=10, columnspan=4, sticky='w')


def add_employee():
    pass


def update_employee():
    pass


def remove_employee():
    pass


def clear_employee():
    pass


# buttons
btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, padx=10, pady=10, columnspan=4, sticky='w')
btnAdd = Button(btn_frame, command=add_employee, text='Add Details', width=15, font=(
    'Calibri', 16, 'bold'), bd=0, bg="#16a885", fg="white").grid(row=0, column=0, padx=10)

btnUpdate = Button(btn_frame, command=update_employee, text='Update Details', width=15, font=(
    'Calibri', 16, 'bold'), bd=0, bg="#2980b9", fg="white").grid(row=0, column=1, padx=10)

btnRemove = Button(btn_frame, command=remove_employee, text='Delete Details', width=15, font=(
    'Calibri', 16, 'bold'), bd=0, bg="#c0392b", fg="white").grid(row=0, column=2, padx=10)

btnClear = Button(btn_frame, command=clear_employee, text='clear Details', width=15, font=(
    'Calibri', 16, 'bold'), bd=0, bg="#f39c12", fg="white").grid(row=0, column=3, padx=10)

# table frame
root.mainloop()
