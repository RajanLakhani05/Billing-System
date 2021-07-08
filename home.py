from tkinter import *
import os
from tkinter import ttk
import tkinter as tk
import pyrebase
from tkinter import messagebox
from PIL import Image, ImageTk

firebaseConfig = {
    "apiKey": "AIzaSyAbO0PMnDAPTXc8Tg4LyV41DYQm8ouGsjQ",
    "authDomain": "sgp6demo.firebaseapp.com",
    "databaseURL": "https://sgp6demo-default-rtdb.firebaseio.com",
    "projectId": "sgp6demo",
    "storageBucket": "sgp6demo.appspot.com",
    "messagingSenderId": "773659537654",
    "appId": "1:773659537654:web:b1be090f9d88f964ef7cd7",
    "measurementId": "G-KHDHN4ZR6L",
}
firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
root = Tk()

root.title("Home")
root.geometry("1530x785+0+0")
root.resizable(0, 0)
root.configure(background="misty rose")


# background=ImageTk.PhotoImage(file="image/w3.jpg")
# bglable=Label(root, image=background).place(x=0, y=0, relwidth=1, relheight=1)


# my_canvas=Canvas(root,width=1032, height=785)
# my_canvas.pack(fill="both",expand=True)
# my_canvas.create_image(0,0,image=background,anchor="nw")


def employee():
    root.destroy()
    employee_window = Tk()
    employee_window.geometry("1530x785+0+0")
    employee_window.title("Employee")
    employee_window.configure(background="misty rose")
    employee_window.email = StringVar()
    employee_window.pass_ = StringVar()
    img2 = Image.open("image/EM1.png")
    img2 = img2.resize((200, 200), Image.ANTIALIAS)
    employee_window.employee = ImageTk.PhotoImage(img2)

    def login():
        email = employee_window.email.get()
        password = employee_window.pass_.get()
        if employee_window.email.get() == "" or employee_window.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required!!!")

        else:
            try:
                login = auth.sign_in_with_email_and_password(email, password)
                employee_window.email.set("")
                employee_window.pass_.set("")
                employee1()

            except:
                messagebox.showerror("Error", "invalid username or password")

    # bg_lbl = Label(admin_window, image=admin_window.bg_icon).pack()

    title = Label(employee_window, text="Employee Login", font=("times new roman", 40, "bold"), bg="#ffcdc8", fg="black",
                  bd=10,
                  relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)

    Login_Frame = Frame(employee_window, bg="white")
    Login_Frame.place(x=560, y=150)

    logolbl = Label(Login_Frame, image=employee_window.employee, bd=0,bg="white").grid(row=0, columnspan=2, pady=40)

    lbluser = Label(Login_Frame, text="Username", compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(
        row=1, column=0, padx=10, pady=10)
    txtuser = Entry(Login_Frame, bd=5, textvariable=employee_window.email, relief=GROOVE, font=("", 15)).grid(row=1,
                                                                                                           column=1,
                                                                                                           padx=20)

    lbluser = Label(Login_Frame, text="Password", compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(
        row=2, column=0, padx=10, pady=10)
    txtpass = Entry(Login_Frame, show="*", bd=5, textvariable=employee_window.pass_, relief=GROOVE, font=("", 15)).grid(
        row=2, column=1,
        padx=20)

    btn_log = Button(Login_Frame, command=login, text="Login", width=15, font=("times new roman", 14, "bold"),
                     bg="yellow", fg="red").grid(row=3, columnspan=2, pady=20, padx=20)

def employee1():
    employee_window1 = Toplevel()
    employee_window1.geometry("1350x750+0+0")
    employee_window1.resizable(0, 0)
    employee_window1.title("Employee")
    employee_window1.configure(background="misty rose")
    #employee_window1.bg = ImageTk.PhotoImage(file="image/back.png")
    title = Label(employee_window1, text="Employee", font=("times new roman", 40, "bold"), bg="#ffcdc8", fg="black",bd=10,relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)
    #variable
    employee_window1.uname = StringVar()
    employee_window1.pass_ = StringVar()
    employee_window1.billnumber = StringVar()
    employee_window1.c_name = StringVar()
    employee_window1.c_number = StringVar()
    employee_window1.p_id = StringVar()
    employee_window1.p_name = StringVar()
    employee_window1.p_price = StringVar()
    employee_window1.p_quantity = StringVar()
    employee_window1.buying_quantity = StringVar()
    employee_window1.total = 0

    def totalprice():
        employee_window1.textarea.insert(END,
                             f"\n==============================================================================================")
        employee_window1.textarea.insert(END, f"\n\t\t\t\t\t \t\t\t Total:{employee_window1.total}")

    def clear1():
        employee_window1.total = 0
        employee_window1.p_id.set("")
        employee_window1.p_name.set("")
        employee_window1.p_price.set("")
        employee_window1.p_quantity.set("")
        employee_window1.buying_quantity.set("")
        employee_window1.c_name.set("")
        employee_window1.c_number.set("")
        employee_window1.billnumber.set("")
        employee_window1.textarea.delete(1.0, END)
        employee_window1.textarea.insert(END, "\t\t\t\t\t\tWelcome\t")
        employee_window1.textarea.insert(END, f"\n\tBill Number:\t{employee_window1.billnumber.get()}")
        employee_window1.textarea.insert(END, f"\n\tCustomer Name:\t{employee_window1.c_name.get()}")
        employee_window1.textarea.insert(END, f"\n\tCustomer Number:\t{employee_window1.c_number.get()}")
        employee_window1.textarea.insert(END,
                             f"\n==============================================================================================")
        employee_window1.textarea.insert(END, f"\n\t\tProduct \t\t\t QTY \t\t\t Price")
        employee_window1.textarea.insert(END,
                             f"\n==============================================================================================")

    def clear():
        employee_window1.p_id.set("")
        employee_window1.p_name.set("")
        employee_window1.p_price.set("")
        employee_window1.p_quantity.set("")
        employee_window1.buying_quantity.set("")

    def bill():
        employee_window1.textarea.delete(1.0, END)
        employee_window1.textarea.insert(END, "\t\t\t\t\t\tWelcome\t")
        employee_window1.textarea.insert(END, f"\n\tBill Number:\t{employee_window1.billnumber.get()}")
        employee_window1.textarea.insert(END, f"\n\tCustomer Name:\t{employee_window1.c_name.get()}")
        employee_window1.textarea.insert(END, f"\n\tCustomer Number:\t{employee_window1.c_number.get()}")
        employee_window1.textarea.insert(END,
                             f"\n==============================================================================================")
        employee_window1.textarea.insert(END, f"\n\t\tProduct \t\t\t QTY \t\t\t Price")
        employee_window1.textarea.insert(END,
                             f"\n==============================================================================================")

    def billdata():

        if employee_window1.p_name.get() == "" or employee_window1.buying_quantity.get() == "" or employee_window1.p_price.get() == "" or employee_window1.p_quantity.get() == "" or employee_window1.billnumber.get() == "" or employee_window1.c_name.get() == "" or employee_window1.c_number.get() == "":
            messagebox.showerror("Error", "Enter all detail")

        elif (int(employee_window1.buying_quantity.get()) > int(employee_window1.p_quantity.get())):
            messagebox.showerror("Error", "Less Product")
        else:

            employee_window1.total = (int(employee_window1.p_price.get()) * int(employee_window1.buying_quantity.get())) + employee_window1.total
            employee_window1.textarea.insert(END,
                                 f"\n\t\t{employee_window1.p_name.get()} \t\t\t {employee_window1.buying_quantity.get()} \t\t\t {int(employee_window1.p_price.get()) * int(employee_window1.buying_quantity.get())}")
            x = int(employee_window1.p_quantity.get()) - int(employee_window1.buying_quantity.get())
            db = firebase.database()
            db.child('supermarket').child(employee_window1.p_id.get()).update({"Productquantity": x})

    def getdetail():
        id = str(employee_window1.p_id.get())
        db = firebase.database()
        name = db.child('supermarket').child(id).child('Productname').get()
        quantity = db.child('supermarket').child(id).child('Productquantity').get()
        price = db.child('supermarket').child(id).child('Productprice').get()
        if employee_window1.p_id.get() == "":
            messagebox.showerror("Error", "Enter Product id")
        elif str(name.val()) == "None":
            messagebox.showerror("Error", "No data found")
        else:
            employee_window1.p_name.set(name.val())
            employee_window1.p_quantity.set(quantity.val())
            employee_window1.p_price.set(price.val())

    def billsave():
        if employee_window1.c_name.get() == "" or employee_window1.c_number.get() == "" or employee_window1.billnumber.get() == "":
            messagebox.showerror("Error", "Enter Customername,number and bill number")
        else:
            op = messagebox.askyesno("Save Bill", "Do you want to save bill?")
            if op > 0:
                employee_window1.billdata = employee_window1.textarea.get(1.0, END)
                f1 = open("bills/" + str(employee_window1.billnumber.get()) + ".txt", "w")
                f1.write(employee_window1.billdata)
                f1.close()
                messagebox.showinfo("Saved", f"Billno. :{employee_window1.billnumber.get()} saved successfully ")
            else:
                return
    ##
    F1 = LabelFrame(employee_window1, text="Customer Details", font=("times new roman", 12),bg="misty rose" ,fg="black")
    F1.place(x=0, y=80, relwidth=1)
    lbluser = Label(F1, text="Bill Number",bg="misty rose" ,compound=LEFT, font=("times new roman", 14)).grid(row=1, column=0, padx=5,
                                                                                              pady=10)
    txtpass = Entry(F1, bd=5, textvariable=employee_window1.billnumber, relief=GROOVE, font=("", 15)).grid(row=1, column=1, padx=20)

    lbluser = Label(F1, text="Customer Name",bg="misty rose" ,compound=LEFT, font=("times new roman", 14)).grid(row=1, column=2, padx=5,
                                                                                                pady=10)
    txtuser = Entry(F1, bd=5, textvariable=employee_window1.c_name, relief=GROOVE, font=("", 15)).grid(row=1, column=3, padx=20)

    lbluser = Label(F1, text="Contact Number",bg="misty rose" ,compound=LEFT, font=("times new roman", 14)).grid(row=1, column=4,
                                                                                                 padx=5, pady=10)
    txtpass = Entry(F1, bd=5, textvariable=employee_window1.c_number, relief=GROOVE, font=("", 15)).grid(row=1, column=5, padx=20)

    btn_log = Button(F1, text="Add", width=10, font=("times new roman", 14, "bold"), bg="light grey", fg="black",
                     command=bill).grid(row=1, column=6, pady=20, padx=20)

    ##
    Login_Frame = LabelFrame(employee_window1, text="Product details",bg="misty rose", font=("times new roman", 12) ,fg="black")
    Login_Frame.place(x=8, y=185)
    lbluser = Label(Login_Frame,bg="misty rose" ,text="Product ID", compound=LEFT, font=("times new roman", 14)).grid(row=1, column=0,
                                                                                                      padx=10, pady=10)
    txtuser = Entry(Login_Frame, bd=5, textvariable=employee_window1.p_id, relief=GROOVE, font=("", 15)).grid(row=1, column=1,
                                                                                                  padx=20)
    btn_get_details = Button(Login_Frame, text="Get Details", width=10, font=("times new roman", 14, "bold"),
                             bg="light grey", fg="black", command=getdetail).grid(row=2, column=1, pady=0, padx=0)

    lbluser = Label(Login_Frame,bg="misty rose", text="Product Name", compound=LEFT, font=("times new roman", 14)).grid(row=3, column=0,
                                                                                                        padx=10,
                                                                                                        pady=10)
    txtpass = Entry(Login_Frame, bd=5, textvariable=employee_window1.p_name, relief=GROOVE, font=("", 15)).grid(row=3, column=1,
                                                                                                    padx=20)
    lbluser = Label(Login_Frame, bg="misty rose",text="Available Quantity", compound=LEFT, font=("times new roman", 14)).grid(row=4,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=10)
    txtpass = Entry(Login_Frame, bd=5, textvariable=employee_window1.p_quantity, relief=GROOVE, font=("", 15)).grid(row=4, column=1,
                                                                                                        padx=20)
    lbluser = Label(Login_Frame,bg="misty rose" ,text="Buying Quantity", compound=LEFT, font=("times new roman", 14)).grid(row=6,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=10)
    txtpass = Entry(Login_Frame, bd=5, textvariable=employee_window1.buying_quantity, relief=GROOVE, font=("", 15)).grid(row=6,
                                                                                                             column=1,
                                                                                                             padx=20)
    lbluser = Label(Login_Frame, bg="misty rose",text="Product Price", compound=LEFT, font=("times new roman", 14)).grid(row=5,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=10)
    txtpass = Entry(Login_Frame, bd=5, textvariable=employee_window1.p_price, relief=GROOVE, font=("", 15)).grid(row=5, column=1,
                                                                                                     padx=20)

    btn_log = Button(Login_Frame, text="Add", command=billdata, width=15, font=("times new roman", 14, "bold"),
                     bg="light grey", fg="black").grid(row=7, column=0, pady=20, padx=20)
    btn_log = Button(Login_Frame, text="Remove", command=clear, width=15, font=("times new roman", 14, "bold"),
                     bg="light grey", fg="black").grid(row=7, column=1, pady=20, padx=20)
    btn_log = Button(Login_Frame, text="Clear", command=clear1, width=15, font=("times new roman", 14, "bold"),
                     bg="light grey", fg="black").grid(row=8, column=0, pady=20, padx=20)
    btn_log = Button(Login_Frame, text="Total", command=totalprice, width=15, font=("times new roman", 14, "bold"),
                     bg="light grey", fg="black").grid(row=8, column=1, pady=20, padx=20)

    ###
    F2 = LabelFrame(employee_window1, bd=10, bg="misty rose",relief=GROOVE)
    F2.place(x=530, y=185, width=800, height=557)
    bill_title = Label(F2, text="Bill Area", font=("arial", 15, "bold"), bd=5, relief=GROOVE).pack(fill=X)
    scroll_y = Scrollbar(F2, orient=VERTICAL)
    employee_window1.textarea = Text(F2, font=("arial", 10), yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=employee_window1.textarea.yview)
    employee_window1.textarea.pack(fill=BOTH, expand=1)
    bill()

    ###
    F3 = LabelFrame(employee_window1, bg="misty rose",text="Generate Bill", font=("times new roman", 12), fg="black")
    F3.place(x=8, y=640)
    btn_log = Button(F3, text="Bill Generate", command=billsave, width=15, font=("times new roman", 14, "bold"),bg="light grey", fg="black").grid(row=8, columnspan=2, pady=20, padx=157)


def admin():

    root.destroy()
    admin_window = Tk()
    admin_window.geometry("1530x785+0+0")
    admin_window.resizable(0, 0)
    admin_window.title("Admin Login")
    admin_window.configure(background="misty rose")
    # =========images======
    admin_window.bg_icon = ImageTk.PhotoImage(file="images/bgb.jpg")
    admin_window.user_icon = ImageTk.PhotoImage(file="images/man-user.png")
    admin_window.pass_icon = ImageTk.PhotoImage(file="images/password.png")
    admin_window.logo_icon = ImageTk.PhotoImage(file="images/logo.jpg")

    # ============variables========
    admin_window.uname = StringVar()
    admin_window.pass_ = StringVar()

    def login():
        if admin_window.uname.get() == "" or admin_window.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required!!!")

        elif admin_window.uname.get() == "admin" and admin_window.pass_.get() == "12345":
            admin_window.uname.set("")
            admin_window.pass_.set("")
            admin1()

        else:
            messagebox.showerror("Error", "invalid username or password")

    # bg_lbl = Label(admin_window, image=admin_window.bg_icon).pack()

    title = Label(admin_window, text="ADMIN Login", font=("times new roman", 40, "bold"), bg="#ffcdc8", fg="black",
                  bd=10,
                  relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)

    Login_Frame = Frame(admin_window, bg="white")
    Login_Frame.place(x=560, y=150)

    logolbl = Label(Login_Frame, image=admin_window.logo_icon, bd=0).grid(row=0, columnspan=2, pady=40)

    lbluser = Label(Login_Frame, text="Username", compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(
        row=1, column=0, padx=10, pady=10)
    txtuser = Entry(Login_Frame, bd=5, textvariable=admin_window.uname, relief=GROOVE, font=("", 15)).grid(row=1,
                                                                                                           column=1,
                                                                                                           padx=20)

    lbluser = Label(Login_Frame, text="Password", compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(
        row=2, column=0, padx=10, pady=10)
    txtpass = Entry(Login_Frame, show="*", bd=5, textvariable=admin_window.pass_, relief=GROOVE, font=("", 15)).grid(
        row=2, column=1,
        padx=20)

    btn_log = Button(Login_Frame, command=login, text="Login", width=15, font=("times new roman", 14, "bold"),
                     bg="yellow", fg="red").grid(row=3, columnspan=2, pady=20, padx=20)


def admin1():
    def logout():

        admin_window1.destroy()



    admin_window1 = Toplevel()
    admin_window1.geometry("1530x785+0+0")
    admin_window1.resizable(0, 0)
    admin_window1.title("Admin")
    admin_window1.configure(background="misty rose")
    #admin_window1.bg = ImageTk.PhotoImage(file="image/back.png")

    img1 = Image.open("image/IN1.png")
    img1 = img1.resize((200, 200), Image.ANTIALIAS)
    img2 = Image.open("image/EM1.png")
    img2 = img2.resize((200, 200), Image.ANTIALIAS)
    img3 = Image.open("image/INVO1.png")
    img3 = img3.resize((200, 200), Image.ANTIALIAS)
    admin_window1.inventory = ImageTk.PhotoImage(img1)
    admin_window1.employee=ImageTk.PhotoImage(img2)
    admin_window1.invoice=ImageTk.PhotoImage(img3)



    img = Image.open("image/logout.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    admin_window1.logout_btn = ImageTk.PhotoImage(img)

    logout = Button(admin_window1, image=admin_window1.logout_btn, borderwidth=0, bg="misty rose",
                    command=logout).place(x=10, y=10)
    invetory=Button(admin_window1,image=admin_window1.inventory,borderwidth=0, bg="misty rose",command=inventory).place(x=250, y=250)
    invtext=Label(admin_window1,text="INVENTORY",font=("times new roman", 14, "bold"),bg="misty rose").place(x=290,y=475)
    em = Button(admin_window1, image=admin_window1.employee, borderwidth=0, bg="misty rose",command=emp).place(x=650, y=250)
    emtext=Label(admin_window1,text="EMPLOYEE",font=("times new roman", 14, "bold"),bg="misty rose").place(x=700,y=475)
    invoic=Button(admin_window1, image=admin_window1.invoice, borderwidth=0, bg="misty rose",command=invoice).place(x=1050, y=250)
    invotext=Label(admin_window1,text="INVOICE",font=("times new roman", 14, "bold"),bg="misty rose").place(x=1110,y=475)


def inventory():
    inventory1=Toplevel()
    inventory1.title("inventory")
    inventory1.geometry("1080x720+0+0")
    inventory1.resizable(0,0)
    inventory1.configure(background="misty rose")
    def fetch():
        db = firebase.database()
        all_users = db.child('supermarket').get()
        #for user in all_users:
        #print(user.val())
         #   table.insert('', END, values=user.val())


    def additem():
        add=Toplevel()
        add.title("ADD ITEM")
        add.geometry("1080x720+0+0")
        add.resizable(0, 0)
        add.configure(background="misty rose")
        frame = Frame(add, bg="white")
        add.name=StringVar()
        add.price=StringVar()
        add.quantity=StringVar()
        def addtodatabase():
            try:
                db = firebase.database()
                data = {"Productid":inventory1.pid.get(),"Productname":add.name.get(),"Productprice":int(add.price.get()),"Productquantity":int(add.quantity.get())}
                db.child('supermarket').child(inventory1.pid.get()).set(data)
                messagebox.showinfo("Successful","Data added")
                add.destroy()
            except:
                messagebox.showerror("Error"," Something Went Wrong")



        frame.place(x=10, y=150, width=1060, height=480)
        title = Label(add, text="ADD ITEM", font=("times new roman", 40, "bold"), bg="#ffcdc8", fg="black",
                      bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)
        lblprdid = Label(frame, text="Product id:", compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=2, column=1, padx=20, pady=40)
        textprdit = Label(frame, text=inventory1.pid.get(), compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=2, column=2,padx=20)
        lblprdid = Label(frame, text="Product Name:", compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=2, column=3, padx=10, pady=40)
        textprdit = Entry(frame, bd=5, relief=GROOVE, textvariable=add.name, font=("", 15)).grid(row=2, column=4,padx=10)

        lblprdid = Label(frame, text="Product Price:", compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=5, column=1, padx=20, pady=40)
        textprdit = Entry(frame, bd=5, relief=GROOVE, textvariable=add.price, font=("", 15)).grid(row=5, column=2,padx=10)

        lblprdid = Label(frame, text="Product Quantity:", compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=5, column=3, padx=20, pady=40)
        textprdit = Entry(frame, bd=5, relief=GROOVE, textvariable=add.quantity, font=("", 15)).grid(row=5, column=4,padx=10)

        btn_add = Button(frame, text="ADD ITEM",command=addtodatabase, width=30, font=("times new roman", 14, "bold"),
                         bg="yellow", fg="red").place(x=370,y=300)

    def updateitem():
        update=Toplevel()
        update.title("ADD ITEM")
        update.geometry("1080x720+0+0")
        update.resizable(0, 0)
        update.configure(background="misty rose")
        frame = Frame(update, bg="white")
        update.name=StringVar()
        update.price=StringVar()
        update.quantity=StringVar()
        def updatetodatabase():
            try:
                db = firebase.database()
                db.child('supermarket').child(inventory1.pid.get()).update({"Productid":inventory1.pid.get(),"Productname":update.name.get(),"Productprice":int(update.price.get()),"Productquantity":int(update.quantity.get())})
                messagebox.showinfo("Successful","Data Updated")
                update.destroy()
            except:
                messagebox.showerror("Error"," Something Went Wrong")


        frame.place(x=10, y=150, width=1060, height=480)
        title = Label(update, text="UPDATE ITEM", font=("times new roman", 40, "bold"), bg="#ffcdc8", fg="black",
                      bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)
        lblprdid = Label(frame, text="Product id:", compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=2, column=1, padx=20, pady=40)
        textprdit = Label(frame, text=inventory1.pid.get(), compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=2, column=2,padx=20)
        lblprdid = Label(frame, text="Product Name:", compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=2, column=3, padx=10, pady=40)
        textprdit = Entry(frame, bd=5, relief=GROOVE, textvariable=update.name, font=("", 15)).grid(row=2, column=4,padx=10)

        lblprdid = Label(frame, text="Product Price:", compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=5, column=1, padx=20, pady=40)
        textprdit = Entry(frame, bd=5, relief=GROOVE, textvariable=update.price, font=("", 15)).grid(row=5, column=2,padx=10)

        lblprdid = Label(frame, text="Product Quantity:", compound=LEFT, font=("times new roman", 20, "bold"),
                         bg="white").grid(row=5, column=3, padx=20, pady=40)
        textprdit = Entry(frame, bd=5, relief=GROOVE, textvariable=update.quantity, font=("", 15)).grid(row=5, column=4,padx=10)

        btn_add = Button(frame, text="UPDATE ITEM",command=updatetodatabase, width=30, font=("times new roman", 14, "bold"),
                         bg="yellow", fg="red").place(x=370,y=300)

    def deleteitem():
        try:
            db = firebase.database()
            db.child('supermarket').child(inventory1.pid.get()).remove()
            messagebox.showinfo("Successful","Data Deleted")
        except:
            messagebox.showerror("Error", " Something Went Wrong")


    def check():
        if inventory1.pid.get()=="":
            messagebox.showerror("Error","Enter Product id")
        else:
            additem()
    def check1():
        if inventory1.pid.get()=="":
            messagebox.showerror("Error","Enter Product id")
        else:
            updateitem()





    inventory1.pid = StringVar()
    title = Label(inventory1, text="Inventory", font=("times new roman", 40, "bold"), bg="#ffcdc8", fg="black",
                  bd=10,relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)
    _Frame = Frame(inventory1, bg="white")
    _Frame.place(x=10, y=150,height=480)
    lblprdid = Label(_Frame, text="Product id:", compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(
        row=1, column=0, padx=10, pady=40)
    textprdit= Entry(_Frame, bd=5, relief=GROOVE,textvariable=inventory1.pid, font=("", 15)).grid(row=1,column=1,padx=20)
    btn_add = Button(_Frame,text="ADD ITEM",command=check, width=30, font=("times new roman", 14, "bold"),
                     bg="yellow", fg="red").grid(row=3, columnspan=2, pady=40, padx=20)
    btn_update = Button(_Frame, text="UPDATE ITEM",command=check1, width=30, font=("times new roman", 14, "bold"),
                     bg="yellow", fg="red").grid(row=5, columnspan=2, pady=40, padx=20)
    btn_delete = Button(_Frame, text="DELETE ITEM",command=deleteitem, width=30, font=("times new roman", 14, "bold"),
                     bg="yellow", fg="red").grid(row=7, columnspan=2, pady=40, padx=20)

    #Tableframe=Frame(inventory1,bg="white")
    #Tableframe.place(x=450,y=150,width=620,height=480)
    #inventory1.textdata=StringVar()
    #text=ttk.Text(Tableframe,font=("times neaw roman", 14, "bold")).place(x=0,y=0)

    #inventory1.textdata.set("Jemil")
    #scroll_x=Scrollbar(Tableframe,orient=HORIZONTAL)
    #scroll_y=Scrollbar(Tableframe,orient=VERTICAL)
    #table=ttk.Treeview(Tableframe,column=("Id","Product Name","Product Price","Product Quantity"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    #scroll_x.pack(side=BOTTOM,fill=X)
    #scroll_y.pack(side=RIGHT,fill=Y)
    #scroll_x.config(command=table.xview)
    #scroll_y.config(command=table.yview)
    #table.heading("Id",text="ID")
    #able.heading("Product Name", text="Product Name")
    #table.heading("Product Price",text="Product Price")
    #table.heading("Product Quantity",text="Product Quantity")
    #table['show']='headings'
    #table.pack(fill=BOTH,expand=1)

    F2 = LabelFrame(inventory1, bd=10, relief=GROOVE)
    F2.place(x=450, y=150, width=620, height=480)
    bill_title = Label(F2, text="Product list", font=("arial", 15, "bold"),bg="#ffcdc8" ,bd=5, relief=GROOVE).pack(fill=X)
    scroll_y = Scrollbar(F2, orient=VERTICAL)
    inventory1.textarea = Text(F2, font=("arial", 11, "bold"), yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=inventory1.textarea.yview)
    inventory1.textarea.pack(fill=BOTH, expand=1)

    db = firebase.database()
    users = db.child('supermarket').get()
    for user in users.each():
        val = str(user.val()) + "\n\n"
        inventory1.textarea.insert(END, val)
    inventory1.textarea.delete(1.0,3.0)








def emp():
    emp=Toplevel()
    emp.title("Employee")
    emp.geometry("1080x720+0+0")
    emp.resizable(0,0)
    emp.configure(background="misty rose")

    img2 = Image.open("image/EM1.png")
    img2 = img2.resize((200, 200), Image.ANTIALIAS)
    emp.employee=ImageTk.PhotoImage(img2)

    # ============variables========
    emp.email = StringVar()
    emp.pass_ = StringVar()



    def create():
        email=emp.email.get()
        password=emp.pass_.get()
        try:
            user = auth.create_user_with_email_and_password(email, password)
            messagebox.showinfo("successfull", "Data Created")
        except Exception as e:
            messagebox.showerror("Error", "Something went Wrong")

    title = Label(emp, text="Employee Id Creation", font=("times new roman", 40, "bold"), bg="#ffcdc8", fg="black",
                  bd=10,
                  relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)

    Login_Frame = Frame(emp, bg="white")
    Login_Frame.place(x=350, y=150)

    logolbl = Label(Login_Frame, image=emp.employee, bd=0,bg="white").grid(row=0, columnspan=2, pady=40)

    lbluser = Label(Login_Frame, text="Email", compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(
        row=1, column=0, padx=10, pady=10)
    txtuser = Entry(Login_Frame, bd=5, textvariable=emp.email, relief=GROOVE, font=("", 15)).grid(row=1,
                                                                                                           column=1,
                                                                                                           padx=20)

    lbluser = Label(Login_Frame, text="Password", compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(
        row=2, column=0, padx=10, pady=10)
    txtpass = Entry(Login_Frame, show="*", bd=5, textvariable=emp.pass_, relief=GROOVE, font=("", 15)).grid(
        row=2, column=1,
        padx=20)

    btn_log = Button(Login_Frame, command=create, text="Create", width=15, font=("times new roman", 14, "bold"),
                     bg="yellow", fg="red").grid(row=3, columnspan=2, pady=20, padx=20)
   # btn_show=Button(Login_Frame,text="Show or Hide password",command=toggle_password,width=20,font=("times new roman", 14, "bold"),
    #                 bg="yellow", fg="red").grid(row=3, columnspan=2, pady=20, padx=23)




def invoice():
    invoice=Toplevel()
    invoice.title("Invoice")
    invoice.geometry("1350x750+0+0")
    invoice.resizable(0, 0)
    invoice.configure(background="misty rose")

    title = Label(invoice, text="Invoice", font=("times new roman", 40, "bold"), bg="#ffcdc8", fg="black", bd=10,
                  relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)

    def view():
        x = billtxt.get()
        for i in os.listdir("bills/"):
            if i.split('.')[0] == x[:-4]:
                f1 = open(f"bills/{i}", "r")
                invoice.textarea.delete(1.0, END)
                for d in f1:
                    invoice.textarea.insert(END, d)
                f1.close()

    F3 = LabelFrame(invoice, text="Invoice search", font=("times new roman", 12), bg="misty rose", fg="black")
    F3.place(x=8, y=100)
    n = tk.StringVar()
    L1 = list()
    for i in os.listdir("bills/"):
        L1.append(i)
    x = tuple(L1)
    billtxt = ttk.Combobox(F3, width=50, height=30, textvariable=n)
    billtxt['values'] = x
    billtxt.grid(column=1, row=5, pady=20, padx=90)

    btnview = Button(F3, text="View Bill", command=view, width=15, font=("times new roman", 14, "bold"),
                     bg="light grey", fg="black").grid(row=7, column=1, pady=20, padx=10)

    F2 = LabelFrame(invoice, bd=10, relief=GROOVE)
    F2.place(x=530, y=110, width=800, height=557)
    bill_title = Label(F2, text="Bill Area", font=("arial", 15, "bold"), bd=5, relief=GROOVE).pack(fill=X)
    scroll_y = Scrollbar(F2, orient=VERTICAL)
    invoice.textarea = Text(F2, font=("arial", 10), yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=invoice.textarea.yview)
    invoice.textarea.pack(fill=BOTH, expand=1)




admin_btn = ImageTk.PhotoImage(file="image/admin (1).png")
my_button = Button(root, image=admin_btn, borderwidth=0, bg="misty rose", command=admin).place(x=530, y=300)

Employee_btn = ImageTk.PhotoImage(file="image/employee.png")
my_button1 = Button(root, image=Employee_btn, borderwidth=0, bg="misty rose", command=employee).place(x=830, y=300)

# my_canvas.create_text(550,400,text="Login as ?", font="arial 40 bold", fill="white")
title = Label(root, text="LOGIN AS?", fg="black", bg="#ffcdc8", bd=10, font=("times new roman", 40, "bold"),
              relief=GROOVE).place(x=0, y=0, relwidth=1)
# Login = Label(root, font="arial 40 bold", text="Login as ?", foreground="white", bg="#e2b29c").place(x=630, y=350)
#db=firebase.database()
#user=db.child('1').child('Productname').get()
#print(user.val())

root.mainloop()
