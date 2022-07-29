from tkinter import *
import mysql.connector
import tkinter.messagebox as mb
import pickle

def main():
    
    #~~~~~~~~~~~~~~~~~~~~~SETTINGS~~~~~~~~~~~~~~~~~~~~~~~

    def settings():
        settings_root = Toplevel()
               
        settings_root.iconbitmap('book.ico')
        settings_root.title("Library Management System")
        
        settings_root.geometry("600x480")
        settings_root.minsize(width="600", height="480")
        settings_root.maxsize(width="600", height="480")
        
        top_frame = Frame(settings_root,bg="black",height="110",width="850")
        top_frame.place(x=0,y=0)

        libheading = Label(top_frame, text="Settings", font="elephant 40 bold", fg="white", bg="black")
        libheading.place(x=190, y=18)

        frame1 = Frame(settings_root, bg="white", height="350", width="600")
        frame1.place(x=-10, y=100)
        
        #Image
        global image1
        image1 = PhotoImage(file="background.gif")
        label_for_image = Label(frame1, image=image1)
        label_for_image.pack()
          
        def change():
            settings_root.destroy()
            
            def check():
                pass1 = password.get()
    
                file = open("passwords.txt","rb+")
                x = pickle.load(file)
    
                if(pass1 == x):
                    root_check.destroy()

                    #------password change-----
                    
                    def new_password():
                        string1 = new_pass.get()
                        string2 = confirm_pass.get()
           
                        if(string1 == string2):
                            file = open("passwords.txt", "rb+")
                            x = pickle.load(file)
                
                            if(string1 == x):
                                mb.showinfo("Same Password", "New Password is same as Current Password")
                                file.close()
                    
                            else:
                                file = open("passwords.txt", "wb+")
                                pickle.dump(string1,file)
                                file.close()
                                root.destroy()
                                run()
                    
                        else:
                            mb.showinfo("Not Matched", "Confirmatory Password not matched")

                    root_pass = Toplevel()

                    root_pass.iconbitmap('book.ico')
                    root_pass.title("Library Management System")
        
                    root_pass.geometry('350x500')
                    root_pass.minsize(width="350", height="500")
                    root_pass.maxsize(width="350", height="500")

                    #Image
                    global img1
                    img1 = PhotoImage(file="pass_img.png")
                    label_for_image = Label(root_pass, image=img1)
                    label_for_image.pack()

                    #Entry
                    new_pass = Entry(root_pass, bd="5", show="*")
                    new_pass.place(x=110,y=202)

                    confirm_pass = Entry(root_pass, bd="5", show="*")
                    confirm_pass.place(x=110, y=300)

                    #Button
                    b2 = Button(root_pass, text='Change Password', bg="black", fg="white", bd="5", font="arial 12 bold", command=new_password)
                    b2.place(x=95, y=350)

                    root_pass.mainloop()

                elif(pass1 != x):
                    mb.showinfo("Bad Login", "Incorrect Password")

                else:
                    print("")

            root_check = Toplevel()

            root_check.iconbitmap('book.ico')
            root_check.title("Library Management System")

            root_check.geometry("352x500")
            root_check.minsize(width="352", height="500")
            root_check.maxsize(width="352", height="500")
        
            #Image
            global image1
            image1 = PhotoImage(file="check.png")
            label_for_image = Label(root_check, image=image1)
            label_for_image.pack()
                
            #Label And Entry
            password = Entry(root_check, bd="5", show="*")
            password.place(x=116, y=210)

            #Button
            b1 = Button(root_check, text="Confirm", bg="black", fg="white", bd="5", font="arial 12 bold", command=check)
            b1.place(x=140, y=260)

        def about():
            settings_root.destroy()
            about_root = Toplevel()

            about_root.iconbitmap('book.ico')
            about_root.title("Library Management System")
       
            about_root.geometry("600x510")
            about_root.minsize(width="600", height="510")
            about_root.maxsize(width="600", height="510")
        
            #Image
            image1 = PhotoImage(file="about.gif")
            label_for_image= Label(about_root, image=image1)
            label_for_image.pack()

            about_root.mainloop()
            
        def set_close():
            close_ques = mb.askquestion("Close", "Are You Sure ?")
            if(close_ques == "yes"):
                settings_root.destroy()
                
        #Images
        ph1 = PhotoImage(file='password_img.png')
        ph2 = PhotoImage(file='info.png')
        
        #Buttons
        password_btn = Button(frame1, bg='black', height="200", width="200", image=ph1, command=change)
        password_btn.place(x=70,y=55)

        about_btn = Button(frame1, bg="black", height="200", width="200", image=ph2, command=about)
        about_btn.place(x=340, y=55)

        close_button = Button(settings_root, text="Close", bg="black", fg="white", bd="5", font="arial 12 bold", command=set_close)
        close_button.place(x=265, y=400)
        
        settings_root.mainloop()
          
    #~~~~~~~~~~~~~~~~~~~~ADD STUDENTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               
    def add_students():

        def stu_close():
            stu_ques = mb.askquestion("Close", "Are You Sure ?")           
            if(stu_ques == "yes"):
                add_stu_root.destroy()
            
        def stu_clear():
            stu_id.delete(0,END)
            stu_name.delete(0,END)
            father_entry.delete(0,END)
            course_entry.delete(0,END)
            branch_entry.delete(0,END)
            semester_entry.delete(0,END)
            year_entry.delete(0,END)
            
        def stu_delete():
            stu_id1 = stu_id.get()
            stu_name1 = stu_name.get()
            father = father_entry.get()
            course = course_entry.get()
            branch = branch_entry.get()
            semester = semester_entry.get()
            year = year_entry.get()
                        
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("delete from add_student where stu_id1='" + stu_id1 + "'")
            ques = mb.askquestion("Delete", "Are You Sure You Want To Delete Data")             
            if(ques == "yes"):
                cursor.execute("commit")
                mb.showinfo("Deleted", "Data Successfully Deleted")

        def stu_insert():
            stu_id1 = stu_id.get()
            stu_name1 = stu_name.get()
            father = father_entry.get()
            course = course_entry.get()
            branch = branch_entry.get()
            semester = semester_entry.get()
            year = year_entry.get()
                        
            con = mysql.connector.connect(host="localhost",user="root",password="123456",db="library")
            cursor = con.cursor()
            cursor.execute("insert into add_student values('" + stu_id1 + "','" + stu_name1 + "','" + father + "','" + course + "','" + branch + "','" + semester + "','" + year + "')")
            cursor.execute("commit");
            mb.showinfo("Inserted", "Data Successfully Inserted")

        add_stu_root = Toplevel()

        add_stu_root.iconbitmap('book.ico')
        add_stu_root.title("Library Management System")
    
        add_stu_root.geometry("950x550")
        add_stu_root.minsize(width="950",height="550")
        add_stu_root.maxsize(width="950",height="550")

        #Main Frame
        stu_main_frame = Frame(add_stu_root, bg="#d5d8de", height="550", width="900")
        stu_main_frame.place(x=0, y=0)

        #Image
        image1 = PhotoImage(file="stu5.gif")
        label_for_image = Label(stu_main_frame, image=image1)
        label_for_image.pack()

        #--------Entry And Labels----------
                
        #Left
        stu_id=Entry(add_stu_root,bd="5")
        stu_id.place(x=438,y=168)

        stu_name=Entry(add_stu_root,bd="5")
        stu_name.place(x=438,y=260)

        father_entry=Entry(add_stu_root,bd="5")
        father_entry.place(x=438,y=345)

        course_entry=Entry(add_stu_root,bd="5")
        course_entry.place(x=438,y=422)

        #Right
        branch_entry=Entry(add_stu_root,bd="5")
        branch_entry.place(x=740,y=168)

        year_entry=Entry(add_stu_root,bd="5")
        year_entry.place(x=740,y=260)

        semester_entry=Entry(add_stu_root,bd="5")
        semester_entry.place(x=740,y=345)

        #Button Frame
        btn_frame=Frame(stu_main_frame,bg="#b0a897",height="65",width="430")
        btn_frame.place(x=450,y=470)

        student_insert=Button(btn_frame,text="Insert",bg="black",fg="white",bd="5",font="arial 12 bold",command=stu_insert)
        student_insert.place(x=20,y=10)

        student_delete=Button(btn_frame,text="Delete",bg="black",fg="white",bd="5",font="arial 12 bold",command=stu_delete)
        student_delete.place(x=125,y=10)

        student_clear=Button(btn_frame,text="Clear",bg="black",fg="white",bd="5",font="arial 12 bold",command=stu_clear)
        student_clear.place(x=230,y=10)

        student_close=Button(btn_frame,text="Close",bg="black",fg="white",bd="5",font="arial 12 bold",command=stu_close)
        student_close.place(x=330,y=10)

        add_stu_root.mainloop()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~ISSUE BOOK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def issue_book():

        def book_issue_close():
            issue_ques = mb.askquestion("Close", "Are You Sure ?")
            if(issue_ques == "yes"):
                issue_root.destroy()

        def book_issue_clear():
            return_book_id.delete(0,END)
            return_stu_id.delete(0,END)
            return_book_name.delete(0,END)
            return_student_name.delete(0,END)
            return_course_entry.delete(0,END)
            return_branch_entry.delete(0,END)
            date_of_return_entry.delete(0,END)


        def return_delete():
            bookID = return_book_id.get()
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("delete from book_issue where bookID='" + bookID + "'")
            ques = mb.askquestion("Delete", "Are You Sure You Want To Delete Data")
            if(ques=="yes"):
                cursor.execute("commit");
                mb.showinfo("Deleted", "Data Successfully Deleted")

        def return_insert():
            bookID = return_book_id.get()
            studentID = return_stu_id.get()
            bookName = return_book_name.get()
            studentName = return_student_name.get()
            course = return_course_entry.get()
            branch = return_branch_entry.get()
            date = date_of_return_entry.get()
                        
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("insert into book_issue values('" +bookID + "','" + studentID + "','" +  bookName + "','" + studentName + "','" + course + "','" + branch + "','" + date + "')")
            cursor.execute("commit");
            mb.showinfo("Inserted", "Data Successfully Inserted")

        issue_root = Toplevel()
        issue_root.iconbitmap('book.ico')
        issue_root.title("Library Management System")

        issue_root.geometry("900x550")
        issue_root.minsize(width="900", height="550")
        issue_root.maxsize(width="900", height="550")

        #Main Frame
        return_main_frame =  Frame(issue_root, bg="#d5d8de", height="550", width="900")
        return_main_frame.place(x=0,y=0)

        #Image
        image1 = PhotoImage(file="issue_book.gif")
        label_for_image = Label(return_main_frame, image=image1)
        label_for_image.pack()

        #-----------Entry And Labels-----------
                
        #Left
        return_book_id = Entry(issue_root, bd="5")
        return_book_id.place(x=435, y=168)

        return_stu_id = Entry(issue_root, bd="5")
        return_stu_id.place(x=435, y=258)

        return_book_name = Entry(issue_root, bd="5")
        return_book_name.place(x=435, y=345)

        return_student_name = Entry(issue_root, bd="5")
        return_student_name.place(x=435, y=425)

        #Right
        return_course_entry = Entry(issue_root, bd="5")
        return_course_entry.place(x=742, y=168)

        return_branch_entry = Entry(issue_root, bd="5")
        return_branch_entry.place(x=742, y=258)

        date_of_return_entry = Entry(issue_root, bd="5")
        date_of_return_entry.place(x=742, y=345)

        #----------Buttons----------------

        #Button Frame
        btn_frame = Frame(return_main_frame, bg="#b0a897", height="65", width="430")
        btn_frame.place(x=450, y=470)

        return_insert = Button(btn_frame, text="Insert", bg="black", fg="white", bd="5", font="arial 12 bold", command=return_insert)
        return_insert.place(x=20, y=10)

        return_delete = Button(btn_frame, text="Delete", bg="black", fg="white", bd="5", font="arial 12 bold", command=return_delete)
        return_delete.place(x=125, y=10)

        return_clear = Button(btn_frame, text="Clear", bg="black", fg="white", bd="5", font="arial 12 bold", command=book_issue_clear)
        return_clear.place(x=230, y=10)

        return_close = Button(btn_frame, text="Close", bg="black", fg="white", bd="5", font="arial 12 bold", command=book_issue_close)
        return_close.place(x=330, y=10)

        issue_root.mainloop()

    #~~~~~~~~~~~~~~~~~~~~BOOK RETURN~~~~~~~~~~~~~~~~~~~~~~~
           
    def book_return():
                
        def return_close():
            close_ques = mb.askquestion("Close", "Are You Sure ?")
            if(close_ques == "yes"):
                return_root.destroy()

        def clear():
            return_book_id.delete(0,END)
            return_stu_id.delete(0,END)
            return_book_name.delete(0,END)
            return_student_name.delete(0,END)
            return_course_entry.delete(0,END)
            return_branch_entry.delete(0,END)
            date_of_return_entry.delete(0,END)
            
        def return_delete():
            bookID_return = return_book_id.get()
                        
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("delete from book_return where bookID_return='" + return_book_id.get() + "'")
            ques = mb.askquestion("Delete", "Are You Sure You Want To Delete Data")
            if(ques == "yes"):
                cursor.execute("commit");
                mb.showinfo("Deleted", "Data Successfully Deleted")

        def return_insert():
            bookID_return = return_book_id.get()
            studentID_return = return_stu_id.get()
            bookName_return = return_book_name.get()
            studentName_return = return_student_name.get()
            course_return = return_course_entry.get()
            branch_return = return_branch_entry.get()
            date_return = date_of_return_entry.get()
                        
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("insert into book_return values('" + bookID_return + "','" + studentID_return + "','" + bookName_return + "','" + studentName_return + "','" + course_return + "','" + branch_return + "','" + date_return + "')")
            cursor.execute("commit");
            mb.showinfo("Inserted ", "Data Successfully Inserted")

        return_root=Toplevel()

        return_root.iconbitmap('book.ico')
        return_root.title("Library Management System")
        
        return_root.geometry("925x550")
        return_root.minsize(width="925", height="550")
        return_root.maxsize(width="925", height="550")

        #Main Frame
        stu_main_frame = Frame(return_root, height="550", width="900")
        stu_main_frame.place(x=0, y=0)

        #Image
        image1 = PhotoImage(file="return_book2.gif")
        label_for_image = Label(stu_main_frame, image=image1)
        label_for_image.pack()

        #----------Entry And Labels-------
                
        #Left
        return_book_id = Entry(return_root, bd="5")
        return_book_id.place(x=435, y=168)

        return_stu_id = Entry(return_root, bd="5")
        return_stu_id.place(x=435, y=260)

        return_book_name = Entry(return_root, bd="5")
        return_book_name.place(x=435, y=345)

        return_student_name = Entry(return_root, bd="5")
        return_student_name.place(x=435, y=426)
                
        #Right
        return_course_entry = Entry(return_root, bd="5")
        return_course_entry.place(x=740, y=168)

        return_branch_entry = Entry(return_root, bd="5")
        return_branch_entry.place(x=740, y=260)

        date_of_return_entry = Entry(return_root, bd="5")
        date_of_return_entry.place(x=740, y=345)

        #------------Buttons-------------

        #Button Frame
        btn_frame = Frame(stu_main_frame, bg="#b0a897", height="65", width="430")
        btn_frame.place(x=450, y=470)

        return_insert = Button(btn_frame, text="Insert", bg="black", fg="white", bd="5", font="arial 12 bold", command=return_insert)
        return_insert.place(x=20, y=10)

        return_delete = Button(btn_frame, text="Delete", bg="black", fg="white", bd="5", font="arial 12 bold", command=return_delete)
        return_delete.place(x=125, y=10)

        return_clear = Button(btn_frame, text="Clear", bg="black", fg="white", bd="5", font="arial 12 bold", command=clear)
        return_clear.place(x=230, y=10)

        return_close = Button(btn_frame, text="Close", bg="black", fg="white", bd="5", font="arial 12 bold", command=return_close)
        return_close.place(x=330, y=10)

        return_root.mainloop()

    #~~~~~~~~~~~~~~~~~~~~~~~STATISTICS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def statatics():
                
        def return_book_data():
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("select * from book_return ")
            row = cursor.fetchall()
            list2.delete(0, list2.size())

            for row in row:
                insertData = row[0]+' ,   '+row[1]+' ,   '+row[2]+' ,   '+row[3]+' ,   '+row[4]+' ,   '+(str(row[5]))+' ,   '+(str(row[6]))+' ;'
                list2.insert(list2.size()+1, insertData)
                    
        def issue_book_data():
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("select * from book_issue ")
            row = cursor.fetchall()
            list1.delete(0, list1.size())

            for row in row:
                insertData2 = row[0]+' ,   '+row[1]+' ,   '+row[2]+' ,   '+row[3]+' ,   '+row[4]+' ,   '+(str(row[5]))+' ,   '+(str(row[6]))+' ;'
                list1.insert(list1.size()+1, insertData2)

        def add_book_data():
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("select * from add_book ")
            row = cursor.fetchall()
            listbox.delete(0, listbox.size())

            for row in row:
                insertData3 = row[0]+' ,   '+row[1]+' ,   '+row[2]+' ,   '+row[3]+' ,   ' +row[4]+' ,   ' +(str(row[5]))+' ,   ' +(str(row[6]))+' ;'
                listbox.insert(listbox.size()+1, insertData3)

        def add_student_data():
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("select * from add_student ")
            row=cursor.fetchall()
            list4.delete(0, list4.size())

            for row in row:
                insertData4 = row[0]+' ,   '+row[1]+' ,   '+row[2]+' ,   '+row[3]+' ,   '+row[4]+' ,   '+(str(row[5]))+' ,   '+(str(row[6]))+' ;'
                list4.insert(list4.size()+1, insertData4)

        def stat_close():
            close_ques = mb.askquestion("Close", "Are You Sure ?")
            if(close_ques == "yes"):
                statatics_root.destroy()
                
        statatics_root = Toplevel()
        
        statatics_root.iconbitmap('book.ico')
        statatics_root.title("Library Management System")
                
        statatics_root.geometry("1290x650")
        statatics_root.minsize(width="1200", height="660")
        statatics_root.maxsize(width="1200", height="660")

        #Image
        global image1
        image1 = PhotoImage(file="stat_back2.png")
        label_for_image = Label(statatics_root, image=image1)
        label_for_image.pack()

        sta_heading_frame = Frame(statatics_root, bg="black", height="110", width="1300")
        sta_heading_frame.place(x=0, y=0)
                
        sta_heading = Label(sta_heading_frame, text="Statistics", font="elephant 40", fg="white", bg="black")
        sta_heading.place(x=475, y=20)

        #------Issue Frame-------
        issue_book_frame = Frame(statatics_root, bg="#f7ece6", height="200", width="490")
        issue_book_frame.place(x=5,y=170)

        issue_heading = Label(statatics_root, text="Books Issued", font="arial 20 bold", fg="white",bg="black")
        issue_heading.place(x=5, y=120)
        
        #List Box Issue Book
        list1 = Listbox(issue_book_frame, height="12", width="95")
        list1.pack(side=LEFT)
        
        #Scrollbar Issue Book
        
        scrollbar3 = Scrollbar(issue_book_frame)  
        scrollbar3.pack(side=RIGHT, fill=BOTH) 
         
        list1.config(yscrollcommand = scrollbar3.set) 
   
        scrollbar3.config(command = list1.yview)
       
        issue_book_data()

        #-------Return Frame---------
        return_book_frame = Frame(statatics_root, bg="#f7ece6", height="200", width="490")
        return_book_frame.place(x=5, y=430)

        return_heading = Label(statatics_root, text="Books Returned", font="arial 20 bold", fg="white", bg="black")
        return_heading.place(x=5, y=385)

        #List Box Return Book
        list2 = Listbox(return_book_frame, height="12", width="95")
        list2.pack(side=LEFT)

        #Scrollbar Return Book
        scrollbar2 = Scrollbar(return_book_frame)  
        scrollbar2.pack(side=RIGHT, fill=BOTH) 
         
        list2.config(yscrollcommand = scrollbar2.set) 
   
        scrollbar2.config(command = list2.yview)
        
        return_book_data()
        
        #-----Add Student Frame-------
        stu_add_frame = Frame(statatics_root, bg="#f7ece6", height="200", width="490")
        stu_add_frame.place(x=603,y=170)

        issue_heading = Label(statatics_root, text="Students Added", font="arial 20 bold", fg="white",bg="black")
        issue_heading.place(x=603, y=120)

        #List Box Add Student
        list4 = Listbox(stu_add_frame, height="12", width="95")
        list4.pack(side=LEFT)

        #Scrollbar Add Student
        scrollbar1 = Scrollbar(stu_add_frame)  
        scrollbar1.pack(side=RIGHT, fill=BOTH) 
         
        list4.config(yscrollcommand = scrollbar1.set) 
   
        scrollbar1.config(command = list4.yview)
        
        add_student_data()
        
        #-------Add Book Frame------
        book_add_frame = Frame(statatics_root, bg="#f7ece6", height="200", width="490")
        book_add_frame.place(x=603, y=430)

        return_heading = Label(statatics_root, text="Books Added", font="arial 20 bold", fg="white", bg="black")
        return_heading.place(x=603, y=385)
   
        #List Box Add_Book
        listbox = Listbox(book_add_frame, height="12", width="95")
        listbox.pack(side=LEFT) 
        
        #Scrollbar Add Book
        scrollbar = Scrollbar(book_add_frame)  
        scrollbar.pack(side=RIGHT, fill=BOTH) 
         
        listbox.config(yscrollcommand = scrollbar.set) 
   
        scrollbar.config(command = listbox.yview)
        
        add_book_data()
        
        #----Close Button------
        close_button = Button(statatics_root, text="Close", bg="black", fg="white", bd="5", font="arial 12 bold", command=stat_close)
        close_button.place(x=1100, y=118)

        statatics_root.mainloop()
                
    #~~~~~~~~~~~~~~~~~~~~~~ADD BOOK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def add_book():
        
        def add_book_close():
            add_book_close_ques = mb.askquestion("Close", "Are You Sure ?")
            if(add_book_close_ques == "yes"):
                add_root.destroy()

        def add_book_clear():
            book_id.delete(0,END)
            book_name.delete(0,END)
            book_isbn.delete(0,END)
            book_publisher.delete(0,END)
            book_edition.delete(0,END)
            book_price.delete(0,END)
            book_page.delete(0,END)
                    
        def delete():
            id1 = book_id.get()
            name = book_name.get()
            book_isbn1 = book_isbn.get()
            publisher = book_publisher.get()
            edition = book_edition.get()
            price = book_price.get()
            page = book_page.get()
                        
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("delete from add_book where id1='" + id1 + "'")
            ques = mb.askquestion("Delete", "Are You Sure You Want To Delete Data?")
            if(ques == "yes"):
                cursor.execute("commit");
                mb.showinfo("Deleted", "Data Successfully Deleted")

        def insert():
            id1 = book_id.get()
            name = book_name.get()
            book_isbn1 = book_isbn.get()
            publisher = book_publisher.get()
            edition = book_edition.get()
            price = book_price.get()
            page = book_page.get()
                        
            con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
            cursor = con.cursor()
            cursor.execute("insert into add_book values('" + id1 + "','" + name + "','" + book_isbn1 + "','" + publisher + "','" + edition + "','" + price + "','" + page + "')")
            cursor.execute("commit");

            mb.showinfo("Inserted", "Data Successfully Inserted")

        add_root = Toplevel()
        
        add_root.iconbitmap('book.ico')
        add_root.title("Library Management System")
    
        add_root.geometry("952x550")
        add_root.minsize(width="952",height="550")
        add_root.maxsize(width="952",height="550")

        #Main Frame
        main_frame = Frame(add_root, bg="#d5d8de", height="550", width="900")
        main_frame.place(x=0, y=0)

        #Image
        image1 = PhotoImage(file="add_book.gif")
        label_for_image = Label(main_frame, image=image1)
        label_for_image.pack()
                
        #-------------Entry And Labels--------------
                
        #Left
        book_id = Entry(add_root,bd="5")
        book_id.place(x=440,y=170)

        book_name=Entry(add_root,bd="5")
        book_name.place(x=440,y=260)

        book_isbn=Entry(add_root,bd="5")
        book_isbn.place(x=440,y=340)

        book_publisher=Entry(add_root,bd="5")
        book_publisher.place(x=440,y=420)

        #Right
        book_edition=Entry(add_root,bd="5")
        book_edition.place(x=745,y=170)

        book_price=Entry(add_root,bd="5")
        book_price.place(x=745,y=260)

        book_page=Entry(add_root,bd="5")
        book_page.place(x=745,y=340)

        #-------------Buttons--------------
                
        #Button Frame
        btn_frame = Frame(main_frame, bg="#b0a897", height="65", width="430")
        btn_frame.place(x=450, y=470)

        insert = Button(btn_frame, text="Insert", bg="black", fg="white", bd="5", font="arial 12 bold", command=insert)
        insert.place(x=40, y=10)

        delete = Button(btn_frame, text="Delete", bg="black", fg="white", bd="5", font="arial 12 bold", command=delete)
        delete.place(x=135, y=10)

        add_book_clear = Button(btn_frame, text="Clear", bg="black", fg="white", bd="5", font="arial 12 bold", command=add_book_clear)
        add_book_clear.place(x=230, y=10)

        add_book_close = Button(btn_frame, text="Close", bg="black", fg="white", bd="5", font="arial 12 bold", command=add_book_close)
        add_book_close.place(x=330, y=10)

        add_root.mainloop()        

    #~~~~~~~~~~~~~~~~~~~~~~~~Main Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
    root = Tk()

    root.iconbitmap('book.ico')
    root.title("Library Management System")
    
    root.geometry("850x650")
    root.minsize(width="850",height="650")
    root.maxsize(width="850",height="650")

    top_frame = Frame(root,bg="black",height="110",width="850")
    top_frame.place(x=0,y=0)

    libheading = Label(top_frame, text="LIBRARY MANAGEMENT SYSTEM", font="arial 30 bold", fg="white", bg="black")
    libheading.place(x=100, y=30)

    #Frame 1
    frame1 = Frame(root, bg="#f7ece6", height="200", width="800")
    frame1.place(x=-10, y=100)

    #Image
    image1 = PhotoImage(file="background.gif")
    label_for_image = Label(frame1, image=image1)
    label_for_image.pack()

    #Imgs
    add_book_img = PhotoImage(file="add6.png")
    sta_img = PhotoImage(file="stat.png")
    add_stu_img = PhotoImage(file="add_stu3.png")
    issue_img = PhotoImage(file="issue.png")
    return_img = PhotoImage(file="return.png")
    info_img = PhotoImage(file="settings.png")

    #Frame1 Buttons
    add_book_btn = Button(frame1, bg="black", height="200", width="220", image=add_book_img, command=add_book)
    add_book_btn.place(x=48,y=35)

    stastics_btn = Button(frame1, bg="black", height="200", width="220", image=add_stu_img, command=add_students)
    stastics_btn.place(x=308, y=35)

    add_student_btn = Button(frame1, bg="black", height="200", width="220", image=sta_img, command=statatics)
    add_student_btn.place(x=588, y=35)

    issue_book_btn = Button(frame1, bg="black", height="200", width="220", image=issue_img, command=issue_book)
    issue_book_btn.place(x=48, y=280)

    return_book = Button(frame1, bg="black", height="200", width="220", image=return_img, command=book_return)
    return_book.place(x=308, y=280)

    about_lib = Button(frame1, bg="black", height="200", width="220", image=info_img, command=settings)
    about_lib.place(x=588, y=280)

    root.mainloop()

#~~~~~~~~~~~~~~~~~~~~~Primary Window~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def run():
    
    #-----------Database and Files------------    
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="123456")
        cursor = con.cursor()
        cursor.execute("Create database library")
        cursor.execute("use library")
        cursor.execute("Create Table add_book(id1 varchar(20) primary key, name varchar(100), book_isbn1 varchar(30), publisher varchar(50), edition varchar(100), price decimal, page integer)")
        cursor.execute("Create Table book_return(bookID_return varchar(20), studentID_return varchar(20), bookName_return varchar(100), studentName_return varchar(50), course_return varchar(30), branch_return varchar(50),date_return date)")
        cursor.execute("Create Table book_issue(bookID varchar(20), studentID varchar(20), bookName varchar(100), studentName varchar(50), course varchar(30), branch varchar(50), date date)")
        cursor.execute("Create Table add_student(stu_id1 varchar(20) primary key, stu_name1 varchar(50), father varchar(50), course varchar(30), branch varchar(50), semester integer, year integer)")

    except:
        con = mysql.connector.connect(host="localhost", user="root", password="123456", db="library")
        cursor = con.cursor()
        
    try:    
        x = False
        if(open("passwords.txt","rb+") and open("user.txt","rb+")):
            x = True
            
    except:
            string = ""
            file = open("passwords.txt","wb+")
            pickle.dump(string,file)

            string2 = "admin"
            file2 = open("user.txt","wb+")
            pickle.dump(string2,file2)

            file.close()
            file2.close()
            
    #--------------Login Page----------------        
    def login():
        user = user_id.get()
        pass1 = password.get()
    
        file = open("passwords.txt","rb+")
        x = pickle.load(file)
    
        file2 = open("user.txt","rb+")
        y = pickle.load(file2)
    
        if(user == y and pass1 == x):
            root_login.destroy()
            main()

        elif(user!="" or pass1 !=""):
            mb.showinfo("Bad Login", "Incorrect Username or Password")

        else:
            print("")
        
    root_login = Tk()

    root_login.iconbitmap('book.ico')
    root_login.title("Library Management System")
    
    root_login.geometry("900x500")
    root_login.minsize(width="860",height="500")
    root_login.maxsize(width="860",height="500")
    
    login_frame=Frame(root_login, height="500", width="900")
    login_frame.place(x=0, y=0)

    #Image
    image1 = PhotoImage(file="log.gif")
    label_for_image = Label(login_frame, image=image1)
    label_for_image.pack()

    #Label And Entry
    user_id = Entry(root_login, bd="5")
    user_id.place(x=650,y=215)

    password = Entry(root_login, bd="5", show="*")
    password.place(x=650, y=300)

    #Label And Entry
    b1 = Button(root_login, text="Login", bg="black", fg="white", bd="5", font="arial 12 bold", command=login)
    b1.place(x=680, y=360)

    root_login.mainloop()

run()
