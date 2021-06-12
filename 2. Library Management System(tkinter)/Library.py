from tkinter import *
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:

    def __init__(self, root):
        self.root= root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        # =============== Variable===============================================

        self.member_var= StringVar()
        self.prn_num_var= StringVar()
        self.id_num_var= StringVar()
        self.fname_var= StringVar()
        self.lname_var= StringVar()
        self.address_var= StringVar()
        self.post_code_var= StringVar()
        self.book_title_var= StringVar()
        self.book_id_var= StringVar()
        self.date_borrowed_var= StringVar()
        self.due_date_var= StringVar()
        self.return_fine_var= StringVar()
        self.actual_price_var= StringVar()
        self.mob_num_var= StringVar()




    
        lbltitle= Label(self.root, text= "LIBRARY MANAGEMENT SYSTEM", bg= "thistle4", fg= "black", bd= 20, relief= RIDGE, font= ("times new roman", 50, "bold"), padx= 2, pady= 6)
        lbltitle.pack(side= TOP, fill= X)

        frame= Frame(self.root, bd= 12, relief= RIDGE, padx= 20, bg= "thistle4")
        frame.place(x=0, y= 130, width= 1530, height= 400)
        #==========================Dataframe left ============================================
        DataFrameLeft= LabelFrame(frame, text= "Library Member's Information", bg= "thistle4", fg= "black", bd= 14, relief= RIDGE, font= ("times new roman", 14, "bold"))
        DataFrameLeft.place(x= 0, y= 5, width= 900, height= 350)

        lblMember= Label(DataFrameLeft,bg= "thistle4",  text= "Member type", font= ("times new roman", 15, "bold"), padx= 2, pady= 6)
        lblMember.grid(row= 0, column= 0,sticky= W)

        comMember= ttk.Combobox(DataFrameLeft, font= ("times new roman", 15, "bold"),textvariable= self.member_var, width= 27, state= "readonly")
        comMember["value"]= ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row= 0, column= 1)


        lbl_prn_number= Label(DataFrameLeft,bg= "thistle4",text= "PRN Number", font= ("times new roman", 14, "bold"))
        lbl_prn_number.grid(row= 1, column= 0,sticky= W)
        txt_prn_number= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"),textvariable= self.prn_num_var , width= 29)
        txt_prn_number.grid(row= 1, column= 1)

        lbl_id_number= Label(DataFrameLeft,bg= "thistle4",  text= "ID Number", font= ("times new roman", 14, "bold"))
        lbl_id_number.grid(row= 2, column= 0,sticky= W)
        txt_id_number= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.id_num_var,width= 29)
        txt_id_number.grid(row= 2, column= 1)

        lbl_fname= Label(DataFrameLeft,bg= "thistle4",  text= "First Name", font= ("times new roman", 14, "bold"))
        lbl_fname.grid(row= 3, column= 0,sticky= W)
        txt_fname= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.fname_var, width= 29)
        txt_fname.grid(row= 3, column= 1)

        lbl_lname= Label(DataFrameLeft,bg= "thistle4", text= "Last Name", font= ("times new roman", 14, "bold"))
        lbl_lname.grid(row= 4, column= 0,sticky= W)
        txt_lname= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"),textvariable= self.lname_var, width= 29)
        txt_lname.grid(row= 4, column= 1)

        lbl_address= Label(DataFrameLeft,bg= "thistle4", text= "Address", font= ("times new roman", 14, "bold"))
        lbl_address.grid(row= 5, column= 0,sticky= W)
        txt_address= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.address_var, width= 29)
        txt_address.grid(row= 5, column= 1)
        

        lbl_postcode= Label(DataFrameLeft,bg= "thistle4", text= "Post Code", font= ("times new roman", 14, "bold"))
        lbl_postcode.grid(row= 6, column= 0,sticky= W)
        txt_postcode= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.post_code_var, width= 29)
        txt_postcode.grid(row= 6, column= 1)

      

        lbl_booktitle= Label(DataFrameLeft,bg= "thistle4", text= "Book title", font= ("times new roman", 14, "bold"))
        lbl_booktitle.grid(row= 0, column= 2,sticky= W)
        txt_booktitle= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"),textvariable= self.book_title_var, width= 29)
        txt_booktitle.grid(row= 0, column= 3)

        lbl_bookid= Label(DataFrameLeft,bg= "thistle4", text= "Book id", font= ("times new roman", 14, "bold"))
        lbl_bookid.grid(row= 1, column= 2,sticky= W)
        txt_bookid= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.book_id_var, width= 29)
        txt_bookid.grid(row= 1, column= 3)

        lbl_date_borrowed= Label(DataFrameLeft,bg= "thistle4", text= "Date Borrowed", font= ("times new roman", 14, "bold"))
        lbl_date_borrowed.grid(row= 2, column= 2,sticky= W)
        txt_date_borrowed= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.date_borrowed_var, width= 29)
        txt_date_borrowed.grid(row= 2, column= 3)

        lbl_due_date= Label(DataFrameLeft,bg= "thistle4", text= "Due Date", font= ("times new roman", 14, "bold"))
        lbl_due_date.grid(row= 3, column= 2,sticky= W)
        txt_due_date= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.due_date_var, width= 29)
        txt_due_date.grid(row= 3, column= 3)

        lbl_fine= Label(DataFrameLeft,bg= "thistle4", text= "Late Return Fine", font= ("times new roman", 14, "bold"))
        lbl_fine.grid(row= 4, column= 2,sticky= W)
        txt_fine= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.return_fine_var, width= 29)
        txt_fine.grid(row= 4, column= 3)

        lbl_actual_price= Label(DataFrameLeft,bg= "thistle4", text= "Actual Price", font= ("times new roman", 14, "bold"))
        lbl_actual_price.grid(row= 5, column= 2,sticky= W)
        txt_actual_price= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.actual_price_var, width= 29)
        txt_actual_price.grid(row= 5, column= 3)

        lbl_mobile= Label(DataFrameLeft,bg= "thistle4", text= "Mobile Number", font= ("times new roman", 14, "bold"))
        lbl_mobile.grid(row= 6, column= 2,sticky= W)
        txt_mobile= Entry(DataFrameLeft, font= ("times new roman", 14, "bold"), textvariable= self.mob_num_var, width= 29)
        txt_mobile.grid(row= 6, column= 3)
        
        # ===================DataFrame Right====================================================================

        DataFrameRight= LabelFrame(frame, text= "Book Details", bg= "thistle4", fg= "black", bd= 14, relief= RIDGE, font= ("times new roman", 14, "bold"))
        DataFrameRight.place(x= 910, y= 5, width= 540, height= 350)

        self.txtBox= Text(DataFrameRight, font= ("ariel", 12, "bold"), width= 32, height= 16, padx= 2, pady= 6)
        self.txtBox.grid(row= 0, column= 2)

        listScrollBar= Scrollbar(DataFrameRight )
        listScrollBar.grid(row= 0, column= 1, sticky= "ns")

        list_books= ["Python Programming", "Java Programming", "Mathematics for Machine Learning", "R Programming", "Machine LEarning in Depth", "Deep Learning with Python", "Machine Learning with R", "Scala Programming ", "Master Web Development", "JavaScript Programming Language", "Intermediate Python", ]

        def SelectBook(event= ""):
            value= str(listBox.get(listBox.curselection()))
            x= value
            if (x=="Python Programming"):
                self.book_id_var.set("A19282")
                self.book_title_var.set("Python Programming")
                
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days= 15)
                d3= d1+ d2
                self.date_borrowed_var.set(d1)
                self.due_date_var.set(d3)
                self.return_fine_var.set("Rs 100")
                self.actual_price_var.set("Rs 850")
            
            elif (x=="Java Programming"):
                self.book_id_var.set("A19282")
                self.book_title_var.set("Java Programming")
                
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days= 15)
                d3= d1+ d2
                self.date_borrowed_var.set(d1)
                self.due_date_var.set(d3)
                self.return_fine_var.set("Rs 100")
                self.actual_price_var.set("Rs 850")
            
            elif (x=="Mathematics for Machine Learning"):
                self.book_id_var.set("A19282")
                self.book_title_var.set("Mathematics for Machine Learning")
                
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days= 15)
                d3= d1+ d2
                self.date_borrowed_var.set(d1)
                self.due_date_var.set(d3)
                self.return_fine_var.set("Rs 100")
                self.actual_price_var.set("Rs 850")
            
            elif (x=="R Programming"):
                self.book_id_var.set("A19282")
                self.book_title_var.set("R Programming")
                
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days= 15)
                d3= d1+ d2
                self.date_borrowed_var.set(d1)
                self.due_date_var.set(d3)
                self.return_fine_var.set("Rs 100")
                self.actual_price_var.set("Rs 850")

            elif (x=="Machine LEarning in Depth"):
                self.book_id_var.set("A19282")
                self.book_title_var.set("Machine LEarning in Depth")
                
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days= 15)
                d3= d1+ d2
                self.date_borrowed_var.set(d1)
                self.due_date_var.set(d3)
                self.return_fine_var.set("Rs 100")
                self.actual_price_var.set("Rs 850")

            elif (x=="Deep Learning with Python"):
                self.book_id_var.set("A19282")
                self.book_title_var.set("Deep Learning with Python")
                
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days= 15)
                d3= d1+ d2
                self.date_borrowed_var.set(d1)
                self.due_date_var.set(d3)
                self.return_fine_var.set("Rs 100")
                self.actual_price_var.set("Rs 850")

            



        listBox= Listbox(DataFrameRight,font= ("ariel", 12, "bold"), width= 20, height= 16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row= 0, column= 0, padx= 4 )
        listScrollBar.config(command= listBox.yview)

        for item in list_books:
            listBox.insert(END, item)


        #=============== Button Frame =============================
        frame_button= Frame(self.root, bd= 12, relief= RIDGE, padx= 20, bg= "thistle4")
        frame_button.place(x=0, y= 530, width= 1530, height= 70)

        btnAddData= Button(frame_button, text= "Add Data",command= self.add_data, font= ("ariel", 12, "bold"), width= 23, bg= "gray25", fg= "white")
        btnAddData.grid(row= 0, column= 0)

        btnShowData= Button(frame_button, command= self.ShowData, text= "Show Data", font= ("ariel", 12, "bold"), width= 23, bg= "gray25", fg= "white")
        btnShowData.grid(row= 0, column= 1)

        btnUpdate= Button(frame_button, text= "Update",command= self.Update, font= ("ariel", 12, "bold"), width= 23, bg= "gray25", fg= "white")
        btnUpdate.grid(row= 0, column= 2)
        
        btnDelete= Button(frame_button, text= "Delete",command=self.delete, font= ("ariel", 12, "bold"), width= 23, bg= "gray25", fg= "white")
        btnDelete.grid(row= 0, column= 3)

        btnReset= Button(frame_button, text= "Reset",command= self.reset, font= ("ariel", 12, "bold"), width= 23, bg= "gray25", fg= "white")
        btnReset.grid(row= 0, column= 4)

        btnExit= Button(frame_button, text= "Exit",command= self.iExit, font= ("ariel", 12, "bold"), width= 23, bg= "gray25", fg= "white")
        btnExit.grid(row= 0, column= 5)

        #==============Info frame==================================
        frame_details= Frame(self.root, bd= 12, relief= RIDGE, padx= 20, bg= "thistle4")
        frame_details.place(x=0, y= 600, width= 1530, height= 195)

        table_frame= Frame(frame_details, bd= 6, relief= RIDGE,  bg= "thistle4")
        table_frame.place(x=0, y= 2, width= 1460, height= 190)

        xscroll= ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        yscroll= ttk.Scrollbar(table_frame, orient= VERTICAL)

        self.library_table= ttk.Treeview(table_frame, column= ("member_type", "prn_number", "id_num", "fname", "lname", "address", "post_code", "book_title", "book_id", "date_borrowed", "due_date", "return_fine", "actual_price", "mob_num"), xscrollcommand= xscroll.set, yscrollcommand= yscroll.set)
        xscroll.pack(side= BOTTOM, fill= X)
        yscroll.pack(side= RIGHT, fill= Y)
        
        xscroll.config(command= self.library_table.xview)
        yscroll.config(command= self.library_table.yview)

        self.library_table.heading("member_type", text= "Member type")
        self.library_table.heading("prn_number", text= "PRN Number")
        self.library_table.heading("id_num", text= "Id Number")
        self.library_table.heading("fname", text= "First Name")
        self.library_table.heading("lname", text= "Last Name")
        self.library_table.heading("address", text= "Address")
        self.library_table.heading("post_code", text= "Post Code")
        self.library_table.heading("book_title", text= "Title of Book")
        self.library_table.heading("book_id", text= "Book ID")
        self.library_table.heading("date_borrowed", text= "Date of Borrow")
        self.library_table.heading("due_date", text= "Due Date")
        self.library_table.heading("return_fine", text= "Fine")
        self.library_table.heading("actual_price", text= "Actual Price")
        self.library_table.heading("mob_num", text= "Mobile Number")

        self.library_table["show"]= "headings"
        self.library_table.pack(fill= BOTH, expand= 1)        

        self.library_table.column("member_type", width= 100)
        self.library_table.column("prn_number", width= 100)
        self.library_table.column("id_num", width= 100)
        self.library_table.column("fname", width= 100)
        self.library_table.column("lname", width= 100)
        self.library_table.column("address", width= 100)
        self.library_table.column("post_code", width= 100)
        self.library_table.column("book_title", width= 100)
        self.library_table.column("book_id", width= 100)
        self.library_table.column("date_borrowed", width= 100)
        self.library_table.column("due_date", width= 100)
        self.library_table.column("return_fine", width= 100)
        self.library_table.column("actual_price", width= 100)
        self.library_table.column("mob_num", width= 100)
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):

        conn= mysql.connector.connect(host= "localhost", user= "root", password= "india@143",database= "member")
        if conn.is_connected():
            print("Successully Connected")
        else:
            print("Not Connected")
        my_cursor= conn.cursor()
        val= (self.member_var.get(),self.prn_num_var.get(),self.id_num_var.get(),self.fname_var.get(),self.lname_var.get(),
            self.address_var.get(),self.post_code_var.get(),self.book_title_var.get(),self.book_id_var.get(),
            self.date_borrowed_var.get(), self.due_date_var.get(),self.return_fine_var.get(),self.actual_price_var.get(),  
            self.mob_num_var.get())
        sql= "insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        my_cursor.execute(sql, val)
                                                                                       
                                                                                                        
        conn.commit()    
        self.fetch_data()
        conn.close()        

        messagebox.showinfo("Success", "Member has been inserted successfully")                                                                                            


    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost", user= "root", password= "india@143",database= "member")
        my_cursor= conn.cursor()
        sql= "SELECT * FROM library"
        my_cursor.execute(sql)

        rows= my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())

            for i in rows:
                self.library_table.insert("", END, value= i) 
            conn.commit()
            conn.close()

    def get_cursor(self, event= ""):
        cursor_row= self.library_table.focus()
        content= self.library_table.item(cursor_row)
        row= content['values']

        self.member_var.set(row[0]),
        self.prn_num_var.set(row[1]),
        self.id_num_var.set(row[2]),
        self.fname_var.set(row[3]),
        self.lname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.post_code_var.set(row[6]),
        self.book_title_var.set(row[7]),
        self.book_id_var.set(row[8]),
        self.date_borrowed_var.set(row[9]),
        self.due_date_var.set(row[10]),
        self.return_fine_var.set(row[11]),
        self.actual_price_var.set(row[12]),
        self.mob_num_var.set(row[13])
    
    def ShowData(self):

        self.txtBox.insert(END, "Member Type:\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN Number:\t\t" + self.prn_num_var.get() + "\n")
        self.txtBox.insert(END, "ID Number:\t\t" + self.id_num_var.get() + "\n")
        self.txtBox.insert(END, "First Name:\t\t" + self.fname_var.get() + "\n")
        self.txtBox.insert(END, "Last Name:\t\t" + self.lname_var.get() + "\n")
        self.txtBox.insert(END, "Address:\t\t" + self.address_var.get() + "\n")
        self.txtBox.insert(END, "Post Code:\t\t" + self.post_code_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t" + self.book_title_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t" + self.book_id_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t\t" + self.date_borrowed_var.get() + "\n")
        self.txtBox.insert(END, "Due Date:\t\t" + self.due_date_var.get() + "\n")
        self.txtBox.insert(END, "Return Fine:\t\t" + self.return_fine_var.get() + "\n")
        self.txtBox.insert(END, "Actual Price:\t\t" + self.actual_price_var.get() + "\n")
        self.txtBox.insert(END, "Mobile Number:\t\t" + self.mob_num_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.actual_price_var.set(""),
        self.address_var.set(""),
        self.fname_var.set(""),
        self.lname_var.set(""),
        self.return_fine_var.set(""),
        self.actual_price_var.set(""),
        self.due_date_var.set(""),
        self.date_borrowed_var.set(""),
        self.id_num_var.set(""),
        self.book_id_var.set(""),
        self.book_title_var.set(""),
        self.mob_num_var.set(""),
        self.post_code_var.set("")
        self.txtBox.delete("1.0", END)


    def iExit(self):
        iExit= tkinter.messagebox.askyesno("Library Management System","Do you want to exit ?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_num_var.get()== "" or self.id_num_var.get()== "":
            messagebox.showerror("Error", "Select the member first")
        else:
            conn= mysql.connector.connect(host= "localhost", user= "root", password= "india@143",database= "member")
            my_cursor= conn.cursor()
            query= "delete from library where PRN_Number=%s"
            val= (self.prn_num_var.get(), )
            my_cursor.execute(query, val)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success", "Member has been deleted")
            
    def Update(self):
        conn= mysql.connector.connect(host= "localhost", user= "root", password= "india@143",database= "member")
        my_cursor= conn.cursor()
        sql="update library set Member=%s, id_num=%s, fname=%s, lname=%s, address=%s, post_code=%s, book_title=%s, book_id=%s, date_borrowed=%s, due_date=%s, return_fine=%s, actual_price=%s, mob_num=%s where PRN_Number=%s"
        val= (self.member_var.get(),self.id_num_var.get(),self.fname_var.get(),self.lname_var.get(),
            self.address_var.get(),self.post_code_var.get(),self.book_title_var.get(),self.book_id_var.get(),
            self.date_borrowed_var.get(), self.due_date_var.get(),self.return_fine_var.get(),self.actual_price_var.get(),  
            self.mob_num_var.get(),self.prn_num_var.get())
        my_cursor.execute(sql, val)

        conn.commit()
        self.fetch_data() 
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been Updated")


if __name__== "__main__":
    root= Tk()
    obj= LibraryManagementSystem(root)
    root.mainloop()