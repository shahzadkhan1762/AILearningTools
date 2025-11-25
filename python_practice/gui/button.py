#simple program to create different TK widget
from tkinter import *;
from tkinter import ttk;
mainFrame=Tk();
button=ttk.Button(mainFrame, text='Click');     
button.pack();
mainFrame.mainloop();
