from tkinter import *;
from tkinter import messagebox;

root=Tk();
root.geometry("500x200");
root.title('File Writing');

editbtn=Button(root, text='Edit');
editbtn.pack();

areaText=Text(root, width=50, height=5, state=DISABLED);
areaText.pack();

def anable():
    areaText.config(state=NORMAL);
    
editbtn.config(command=anable);

def saveftn():
    data=areaText.get(1.0, END);
    file=open("data.txt", "w");
    file.write(data);
    file.close();
    
savebtn=Button(root, text='Save File', command=saveftn);
savebtn.pack();

exitbtn=Button(root, text='Exit', command=root.destroy); #state=DISABLED
exitbtn.pack();

root.mainloop();