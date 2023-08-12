from tkinter import *

root = Tk()
root.title("Employee management system")
root.geometry("1200x700+0+0")  # 0+0 denotes starts at (0,0)
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
gender = StringVar()
age = StringVar()
doj = StringVar()
email = StringVar()
contact = StringVar()

# entries frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="employee management system",
              font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20)
lblName = Label(entries_frame, text="Name", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0)
txtName = Entry(entries_frame, textvariable=name,
                font=('Calibri', 16), width=30)
txtName.grid(row=1, column=1)

lblAge = Label(entries_frame, text="Age", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2)
txtAge = Entry(entries_frame, textvariable=age, font=('Calibri', 16), width=30)
txtAge.grid(row=1, column=3)

lblGender = Label(entries_frame, text="Gender", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblGender.grid(row=2, column=0)
txtGender = Entry(entries_frame, textvariable=gender,
                  font=('Calibri', 16), width=30)
txtGender.grid(row=2, column=1)

lblDoj = Label(entries_frame, text="Doj", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblDoj.grid(row=2, column=2)
txtDoj = Entry(entries_frame, textvariable=doj, font=('Calibri', 16), width=30)
txtDoj.grid(row=2, column=3)

lblEmail = Label(entries_frame, text="Email", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblEmail.grid(row=3, column=0)
txtEmail = Entry(entries_frame, textvariable=email,
                 font=('Calibri', 16), width=30)
txtEmail.grid(row=3, column=1)

lblContact = Label(entries_frame, text="Contact", font=(
    'Calibri', 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2)
txtContact = Entry(entries_frame, textvariable=contact,
                   font=('Calibri', 16), width=30)
txtContact.grid(row=3, column=3)

# table frame
root.mainloop()
