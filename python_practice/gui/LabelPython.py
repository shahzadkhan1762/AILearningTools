from tkinter import *;
root=Tk();
root.geometry("500x200");
root.title("Label in Python");

label=Label(root, text="Hello Python");
label.pack();

label1=Label(root, text="this is Coloured Text", fg='red');
label1.pack();

label2=Label(root, text="This is Highlighted Text", bg='yellow');
label2.pack();

label3=Label(root, text='This is Raised Text', relief='raised');
label3.pack();

root.mainloop();