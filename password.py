'''
Safety part of program with password
'''

from tkinter import *
import sys


#commands for buttons

def command1(event):

    if entry1.get() == 'admin' and entry2.get() == '1234':

        root.deiconify()

        top.destroy()


def command2():

    top.destroy()

    root.destroy()

    sys.exit()


def command3():

    root.destroy()



#frontend part


root = Tk()

top = Toplevel()

#logg in part

top.geometry('300x280')

top.title('Password keeper')

top.configure(background='white')

photo_entry = PhotoImage(file='lock.gif')

photo = Label(top,image=photo_entry, bg='white')

lbl1 = Label(top, text = 'username:', font = {'Helvetica',10})

entry1 = Entry(top)

lbl2 = Label(top, text = 'password:', font = {'Helvetica',10})

entry2 = Entry(top, show = "*")

button2 = Button(top,text='cancel', command=lambda:command3())


entry2.bind('<Return>', command1)



photo.pack()

lbl1.pack()

entry1.pack()

lbl2.pack()

entry2.pack()

button2.pack()




#log in confirmation


root.geometry('300x180')

root.title('Password keeper')

root.configure(background='white')

photo_entry2 = PhotoImage(file='unlock.gif')

photo2 = Label(root,image=photo_entry2, bg='white')

lbl3 = Label(root, text = 'You have successfully logged in!', font = {'Helvetica',14})


button3 = Button(root,text='next', command=lambda:command3())



photo2.pack()

lbl3.pack()

button3.pack()






root.withdraw()

root.mainloop()
 

