from tkinter import *;
from tkinter import messagebox;
root=Tk();
root.geometry("500x200");
root.title("Button in Python");

label=Label(text="Bellow are some Buttons", relief='raised');
label.pack();

def warning():
    messagebox.showwarning('warning','this is a warning');

def info():
    messagebox.showinfo('Info', 'This is an Information box');
    
def error():
    messagebox.showerror(root, 'Error', 'This is an error Box');

wrn_btn=Button(root, text="Warning", command=warning, fg='red');
wrn_btn.pack();

info_btn=Button(root, text='Info', command=info);
info_btn.pack();

error_btn=Button(root, text='Error', command=error);
error_btn.pack();

cls_btn=Button(root, text="Exit", command=root.destroy, bg='red');
cls_btn.pack();

root.mainloop();
