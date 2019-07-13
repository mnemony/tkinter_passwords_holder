'''
main part of project 
'''

from db_engine import Database
from password import *

database=Database("passdata.db")




class Window(object):

    def __init__(self,window):
        #initializing fronted part of project
        self.window = window

        self.window.wm_title("Password keeper")


        l1=Label(window,text="Web_Adress")
        l1.grid(row=0,column=0)

        l2=Label(window,text="login")
        l2.grid(row=0,column=2)

        l3=Label(window,text="password")
        l3.grid(row=1,column=0)

        l4=Label(window,text="email")
        l4.grid(row=1,column=2)

        self.web_adress_text=StringVar()
        self.e1=Entry(window,textvariable=self.web_adress_text)
        self.e1.grid(row=0,column=1)

        self.login_text=StringVar()
        self.e2=Entry(window,textvariable=self.login_text)
        self.e2.grid(row=0,column=3)

        self.password_text=StringVar()
        self.e3=Entry(window,textvariable=self.password_text)
        self.e3.grid(row=1,column=1)

        self.email_text=StringVar()
        self.e4=Entry(window,textvariable=self.email_text)
        self.e4.grid(row=1,column=3)

        self.list1=Listbox(window, height=8,width=65)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1=Button(window,text="View all", width=12,command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window,text="Search entry", width=12,command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window,text="Add entry", width=12,command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window,text="Update chosen", width=12,command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window,text="Delete chosen", width=12,command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window,text="Close", width=12,command=window.destroy)
        b6.grid(row=7,column=3)


    def get_selected_row(self,event):
        #modeling  method for selecting rows
        
        index=self.list1.curselection()[0]
        self.selected_tuple=self.list1.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4])

    def view_command(self):
        #implementing front part of 'view' method from db_engine
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        #implementing front part of 'search' method from db_engine
        self.list1.delete(0,END)
        for row in database.search(self.web_adress_text.get(),self.login_text.get(),self.password_text.get(),self.email_text.get()):
            self.list1.insert(END,row)

    def add_command(self):
        #implementing front part of 'insert' method from db_engine
        database.insert(self.web_adress_text.get(),self.login_text.get(),self.password_text.get(),self.email_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.web_adress_text.get(),self.login_text.get(),self.password_text.get(),self.email_text.get()))

    def delete_command(self):
        #implementing front part of 'delete' method from db_engine
        database.delete(self.selected_tuple[0])

    def update_command(self):
        #implementing front part of 'update' method from db_engine
        database.update(self.selected_tuple[0],self.web_adress_text.get(),self.login_text.get(),self.password_text.get(),self.email_text.get())


window=Tk()

Window(window)
window.mainloop()
