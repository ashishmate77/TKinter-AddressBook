import pymysql
from tkinter import *
from tkinter import messagebox
cn=None # global variable which hold database connection
def getConnection():
    global cn
    cn=pymysql.connect(database="addressbook",user="root",password="root")

def add_address():

    window=Tk()
    window.title("Add Address Window")
    window.geometry("200x200")
    l1=Label(window,text="Name",font=("Arial",15))
    l2=Label(window,text="Hno",font=("Arial",15))
    l3=Label(window,text="Street",font=("Arial",15))
    l4=Label(window,text="City",font=("Arial",15))
    e1=Entry(window,width=20,font=("Arial",10))
    e2=Entry(window, width=20, font=("Arial", 10))
    e3=Entry(window, width=20, font=("Arial", 10))
    e4=Entry(window, width=20, font=("Arial", 10))
    def insert_data():
        sql="insert into address_info values(%s,%s,%s,%s)"
        c=cn.cursor()
        t=(e1.get(),e2.get(),e3.get(),e4.get())
        c.execute(sql,params=t)
        messagebox.showinfo(title="Info",message="Address Added")
        cn.commit()
    b1=Button(window,text="Add",command=insert_data)
    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    l3.grid(row=3,column=1)
    l4.grid(row=4,column=1)
    e1.grid(row=1,column=2)
    e2.grid(row=2,column=2)
    e3.grid(row=3,column=2)
    e4.grid(row=4,column=2)
    b1.grid(row=5,column=1)
    window.mainloop()
def update_address():
    window=Tk()
    window.title("Update Address")
    window.geometry("200x200")
    l1=Label(window,text="Name",font=("Arial",15))
    l2=Label(window,text="Hno",font=("Arial",15))
    l3 = Label(window, text="Street", font=("Arial", 15))
    l4 = Label(window, text="City", font=("Arial", 15))
    e1 = Entry(window, width=20, font=("Arial", 10))
    e2 = Entry(window, width=20, font=("Arial", 10))
    e3 = Entry(window, width=20, font=("Arial", 10))
    e4 = Entry(window, width=20, font=("Arial", 10))
    def update_data():
        sql="update address_info set houseno=%s,street=%s,city=%s where name=%s"
        t=(e2.get(),e3.get(),e4.get(),e1.get())
        c=cn.cursor()
        c.execute(sql,params=t)
        count=c.rowcount
        if count==0:
            messagebox.showerror(title="Error",message="Invalid Name")
        else:
            messagebox.showinfo(title="Info",message="address is updated")
            cn.commit()
    b1=Button(window,text="Update",command=update_data)
    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)
    l3.grid(row=3, column=1)
    l4.grid(row=4, column=1)
    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=3, column=2)
    e4.grid(row=4, column=2)
    b1.grid(row=5, column=1)
    window.mainloop()
def delete_address():
    window=Tk()
    window.title("Delete Address")
    window.geometry("300x200")
    l1=Label(window,text="Name",font=("Arial",20))
    e1=Entry(window,width=15,font=("Arial",20))
    def delete_data():
        sql="delete from address_info where name=%s"
        t=(e1.get(),)
        c=cn.cursor()
        c.execute(sql,params=t)
        count=c.rowcount
        if count==0:
            messagebox.showerror("Error","Invalid name")
        else:
            messagebox.showinfo("Info","Address it deleted")
            cn.commit()
    b1=Button(window,text="Delete",command=delete_data)
    l1.grid(row=1,column=1)
    e1.grid(row=1,column=2)
    b1.grid(row=2,column=1)
    window.mainloop()
def view_address():
    window = Tk()
    window.title("View Address")
    window.geometry("200x200")
    l1 = Label(window, text="Name", font=("Arial", 15))
    l2 = Label(window, text="Hno", font=("Arial", 15))
    l3 = Label(window, text="Street", font=("Arial", 15))
    l4 = Label(window, text="City", font=("Arial", 15))
    e1 = Entry(window, width=20, font=("Arial", 10))
    e2 = Entry(window, width=20, font=("Arial", 10))
    e3 = Entry(window, width=20, font=("Arial", 10))
    e4 = Entry(window, width=20, font=("Arial", 10))
    def view():
        sql="select houseno,street,city from address_info where name=%s"
        t=(e1.get(),)
        c=cn.cursor()
        c.execute(sql,params=t)
        row=c.fetchone()
        if row==None:
            messagebox.showerror("error","invalid name")
        else:
            e2.insert(0,row[0])
            e3.insert(0,row[1])
            e4.insert(0,row[2])

    b1=Button(window,text="view",command=view)
    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)
    l3.grid(row=3, column=1)
    l4.grid(row=4, column=1)
    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=3, column=2)
    e4.grid(row=4, column=2)
    b1.grid(row=5, column=1)
    window.mainloop()

def main_window():
    window=Tk()
    window.title("Address Book")
    window.geometry("300x300")
    b1=Button(window,text="Add Address",command=add_address)
    b2=Button(window,text="Update Address",command=update_address)
    b3=Button(window,text="Delete Address",command=delete_address)
    b4=Button(window,text="View Address",command=view_address)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    window.mainloop()
def main():
    getConnection()
    main_window()
main()
