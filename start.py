from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random
import time


class pyPhoneBook:
    def __init__(self, root):
        self.root = root
        self.root.title = ('Py Phonebook')
        self.root.geometry('1350x750+0+0')
        self.root.configure(background = 'gainsboro')

        #VARIABLES

        RefNo = StringVar()
        firstname= StringVar()
        lastname= StringVar()
        address= StringVar()
        telephone= StringVar()
        regDate= StringVar()
        idproof= StringVar()
        cDate= StringVar()
        memberType= StringVar()
        memberFee= StringVar()
        Search = StringVar()
        DateDay= StringVar()
        DateToDay = StringVar()


        #Frame and boxes
        mainFrame= Frame(self.root, bd=10, width=1350, height= 700, relief=RIDGE)
        mainFrame.grid(row=0, column=0)

        topFrame1 = Frame(mainFrame, bd=5, width=1340, height=200, relief=RIDGE, bg='cadet blue')
        topFrame1.grid(row=0, column=0)

        topFrame2 = Frame(mainFrame, bd=5, width=1340, height=50, relief=RIDGE, bg='cadet blue')
        topFrame2.grid(row=1, column=0)

        topFrame3 = Frame(mainFrame, bd=5, width=1340, height=300, relief=RIDGE, bg='cadet blue')
        topFrame3.grid(row=2, column=0)

        intopFrame1 = Frame(topFrame1, bd=5, width=1330, height=190, relief=RIDGE, bg='cadet blue')
        intopFrame1.grid()

        intopFrame2 = Frame(topFrame2, bd=5, width=1330, height=48, relief=RIDGE, bg='cadet blue')
        intopFrame2.grid()

        intopFrame3 = Frame(topFrame3, bd=5, width=1330, height=280, relief=RIDGE, bg='cadet blue')
        intopFrame3.grid()

        regDate.set(time.strftime('%d/%m/%Y'))
        DateToDay.set(time.strftime('%d/%m/%Y'))

        def Reset():
            RefNo.set("")
            firstname.set("")
            lastname.set("")
            address.set("")
            telephone.set("")
            regDate.set("")
            idproof.set("")
            cDate.set("")
            memberType.set("")
            memberFee.set("")
            Search.set("")
            DateDay.set("")
            DateToDay.set("")
            regDate.set(time.strftime('%d/%m/%Y'))
            DateToDay.set(time.strftime('%d/%m/%Y'))

        def fExit():
            fExit = tkinter.messagebox.askyesno("Phone Book", "Confirm if you want to exit")
            if fExit >0:
                root.destroy()
                return

        def addData():
                sqlCon = pymysql.connect(host="localhost", user="root", password="", database="pyphonebook")
                cur = sqlCon.cursor()
                cur.execute("insert into pyphonebook (RefNo, firstname, lastname, address, telephone, regDate, idproof, cDate, memberType, memberFee) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (RefNo.get(), firstname.get(), lastname.get(), address.get(), telephone.get(), regDate.get(), idproof.get(), cDate.get(), memberType.get(), memberFee.get()))
                sqlCon.commit()
                sqlCon.close
                tkinter.messagebox.showinfo("Phone Book", "Added Successfully.")
        def update():

            sqlCon = pymysql.connect(host="localhost", user="root", password="", database="entrydata")
            cur = sqlCon.cursor()
            cur.execute("update pyphonebook set firstname=%s, lastname=%s, address=%s, telephone= %s, regdate=%s, idproof=%s, cDate = %s, memberType=%s, member fee=%s where RefNo= %s", (firstname.get(), lastname.get(), address.get(), telephone.get(), regDate.get(), idproof.get(), DateDay.get(), memberType.get(), memberFee.get(), RefNo.get()))

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Py Phone Book", "Record Successfully Updated")

        def deleteDB():
            sqlCon = pymysql.connect(host="localhost", user="root", password="", database="entrydata")
            cur = sqlCon.cursor()
            cur.execute("delete from pyphonebook where RefNo= %s", RefNo.get())

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Py Phone Book", "Record Successfully Deleted")

        def searchDB():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="", database="entrydata")
                cur = sqlCon.cursor()
                cur.execute("select from pyphonebook where RefNo=%s", Search.get())

                row = cur.fetchall()

                RefNo.set(row[0])
                firstname.set(row[1])
                lastname.set(row[2])
                address.set(row[3])
                telephone.set(row[4])
                regDate.set(row[5])
                idproof.set(row[6])
                DateDay.set(row[7])
                memberType.set(row[8])
                memberFee.set(row[9])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Phone Book", "No Data")
                Reset()
                sqlCon.close()


        #LABELS & Entry box

        lblref = Label(intopFrame1, font=('arial', 12, 'bold'), text='Reference No', bd=(10))
        lblref.grid(row=0, column=0, sticky=W)
        txtref = Entry(intopFrame1, font=('arial', 12, 'bold'), bd=5, width=32, justify='left')
        txtref.grid(row=0, column=1)

        lblfn = Label(intopFrame1, font=('arial', 12, 'bold'), text='First Name', bd=(10))
        lblfn.grid(row=1, column=0, sticky=W)
        txtfn = Entry(intopFrame1, font=('arial', 12, 'bold'), bd=5, width=32, justify='left')
        txtfn.grid(row=1, column=1)

        lblln = Label(intopFrame1, font=('arial', 12, 'bold'), text='Last Name', bd=(10))
        lblln.grid(row=2, column=0, sticky=W)
        txtln = Entry(intopFrame1, font=('arial', 12, 'bold'), bd=5, width=32, justify='left')
        txtln.grid(row=2, column=1)

        self.lblTphone = Label(intopFrame1, font=('arial', 12, 'bold'), text = 'Telephone', bd = 10)
        self.lblTphone.grid(row=0, column=2, sticky=W)
        self.txtTphone = Entry(intopFrame1, font=('arial', 12, 'bold'), bd=5, width=32, justify='left')
        self.txtTphone.grid(row=0, column=3)

        self.lblregD = Label(intopFrame1, font=('arial', 12, 'bold'), text='Registration Date', bd=10)
        self.lblregD.grid(row=1, column=2, sticky=W)
        self.txtregD = Entry(intopFrame1, font=('arial', 12, 'bold'), bd=5, width=32, justify='left', textvariable=regDate)
        self.txtregD.grid(row=1, column=3)

        self.lblidProof = Label(intopFrame1, font=('arial', 12, 'bold'), text='Prove of ID', bd=10)
        self.lblidProof.grid(row=2, column=2, sticky=W)
        self.cboxidProof = ttk.Combobox(intopFrame1, font=('arial', 12, 'bold'), width = 31)
        self.cboxidProof['value'] = ('', 'Driving Licence', 'Student Id', 'Passport')
        self.cboxidProof.current(0)
        self.cboxidProof.grid(row=2, column=3)

        self.lblSrc = Label(intopFrame1, font=('arial', 12, 'bold'), text='Search', bd=10)
        self.lblSrc.grid(row=0, column=4, sticky=W)
        self.txtSrc = Entry(intopFrame1, font=('arial', 12, 'bold'), bd=5, width=32, justify='left')
        self.txtSrc.grid(row=0, column=5)

        self.lblDate = Label(intopFrame1, font=('arial', 12, 'bold'), text='Date', bd=10)
        self.lblDate.grid(row=1, column=4, sticky=W)
        self.txtDate = Entry(intopFrame1, font=('arial', 12, 'bold'), bd=5, width=32, justify='left', textvariable=DateToDay)
        self.txtDate.grid(row=1, column=5)

        self.lblmType = Label(intopFrame1, font=('arial', 12, 'bold'), text='Member Type', bd=10)
        self.lblmType.grid(row=2, column=4, sticky=W)
        self.lblmType = ttk.Combobox(intopFrame1, font=('arial', 12, 'bold'), width=31)
        self.lblmType['value'] = ('', 'Annual', 'Quarterly', 'Monthly')
        self.lblmType.current(0)
        self.lblmType.grid(row=2, column=5)

        self.lblsFee = Label(intopFrame1, font=('arial', 12, 'bold'), text='Subscription Pack', bd=10)
        self.lblsFee.grid(row=3, column=4, sticky=W)
        self.lblsFee = ttk.Combobox(intopFrame1, font=('arial', 12, 'bold'), width=31)
        self.lblsFee['value'] = ('', '1000 tk', '300 tk', '700 tk')
        self.lblsFee.current(0)
        self.lblsFee.grid(row=3, column=5)

        self.lbladdr = Label(intopFrame1, font=('arial', 12, 'bold'), text='Address', bd=10)
        self.lbladdr.grid(row=3, column=0, sticky=W)
        self.txtaddr = Entry(intopFrame1, font=('arial', 12, 'bold'), bd=5, width=32, justify='left')
        self.txtaddr.grid(row=3, column=1, columnspan = 3)

        #BUTTONS

        self.btnaNew = Button(intopFrame2, pady=1, bd=4, font=('arial', 16, 'bold'), width =13, text='Add New', command= addData)
        self.btnaNew.grid(row=0, column=0, padx=3)

        self.btndPlay = Button(intopFrame2, pady=1, bd=4, font=('arial', 16, 'bold'), width=13, text='Display')
        self.btndPlay.grid(row=0, column=1, padx=3)

        self.btnUpdate = Button(intopFrame2, pady=1, bd=4, font=('arial', 16, 'bold'), width=13, text='Update')
        self.btnUpdate.grid(row=0, column=2, padx=3)

        self.btnDelete = Button(intopFrame2, pady=1, bd=4, font=('arial', 16, 'bold'), width=13, text='Delete', command= deleteDB)
        self.btnDelete.grid(row=0, column=3, padx=3)

        self.btnRst = Button(intopFrame2, pady=1, bd=4, font=('arial', 16, 'bold'), width=13, text='Reset', command= Reset)
        self.btnRst.grid(row=0, column=4, padx=3)

        self.btnExit = Button(intopFrame2, pady=1, bd=4, font=('arial', 16, 'bold'), width=13, text='Exit', command = fExit)
        self.btnExit.grid(row=0, column=5, padx=3)

        self.btnSrc = Button(intopFrame2, pady=1, bd=4, font=('arial', 16, 'bold'), width=13, text='Search', command=searchDB)
        self.btnSrc.grid(row=0, column=6, padx=3)

        scroll_x = Scrollbar(intopFrame3, orient= HORIZONTAL)
        scroll_y = Scrollbar(intopFrame3, orient= VERTICAL)

        tree_records = ttk.Treeview(intopFrame3, height=13, columns=('RefNo', 'firstname', 'lastname', 'address', 'telephone', 'regDate', 'idproof', 'CurrentDate', 'memberType', 'memberFee'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill=Y)

        tree_records.heading('RefNo', text='Reference No')
        tree_records.heading('firstname', text='First Name')
        tree_records.heading('lastname', text='Last Name')
        tree_records.heading('address', text='Address')
        tree_records.heading('telephone', text='Telephone')
        tree_records.heading('regDate', text='Reg. Date')
        tree_records.heading('idproof', text='ID Proof')
        tree_records.heading('CurrentDate', text='Current Date')
        tree_records.heading('memberType', text='Member Type')
        tree_records.heading('memberFee', text='Member Fee')

        tree_records['show']= 'headings'
        tree_records.column('RefNo', width=150)
        tree_records.column('firstname', width=150)
        tree_records.column('lastname', width=150)
        tree_records.column('address', width=252)
        tree_records.column('telephone', width=100)
        tree_records.column('regDate', width=100)
        tree_records.column('idproof', width=100)
        tree_records.column('CurrentDate', width=100)
        tree_records.column('memberType', width=150)
        tree_records.column('memberFee', width=100)

        tree_records.pack(fill = BOTH, expand=1)







if __name__ == '__main__':
    root = Tk()
    app = pyPhoneBook(root)
    root.mainloop()