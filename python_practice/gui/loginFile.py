from tkinter import *;
from tkinter import messagebox;
root=Tk();
root.geometry("500x200");
root.title('Login');

name='Abbas';
pwd='A123';

nameLabel=Label(root, text='Name', fg='red');
nameLabel.pack();
nameText=Text(root, width=30, height=1, fg='red');
nameText.pack();

pwdLabel=Label(root, text='Password', fg='red');
pwdLabel.pack();
pwdText=Text(root, height=1, width=30, fg='red');
pwdText.pack();

def CheckLogInfo():
    if name==nameText.get(1.0, 'end-1c') and pwd==pwdText.get(1.0, 'end-1c'):
        messagebox.showinfo('Welcome', 'Login Successful');
    else:
        messagebox.showwarning('Sorry', 'Login Unsuccessful');
    nameText.delete(1.0, END);
    pwdText.delete(1.0, END);

logBtn=Button(root, text='Login', command=CheckLogInfo);
logBtn.pack();

root.mainloop();