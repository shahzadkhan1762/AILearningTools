#HOW TO POSITION WIDGETS IN TKINTER
#Psitioning Widget With Layout Managers

#Tkinter has three built=in layout managers that use geometric methods to position widgets in an application frame:
#(1): pack() organizes widgets in horizontal and vertical boxes that are limited to left, right, top, bottom positions. 
#(2): place() places widgets in a two dimensional grid using x and y absolute coordinates.
#(3): grid() locates widgets in a two dimensional grid using row and column absolute coordinates.



from tkinter import *;
root=Tk();
root.geometry("500x200");
root.title("Widget Placement");

label2=Label(root, text='HI There');
label2.pack();

label=Label(root, text='Hi People');
label.place(x=20, y=120);


root.mainloop();