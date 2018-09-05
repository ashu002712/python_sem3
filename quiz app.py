
from tkinter import *

def sel():
   selection = "Correct Answer " + str(var.get()==1)
   label.config(text = selection)

root = Tk()
root.title("QUIZ APPLICATION")
var = IntVar()

Label(root,text=""" What's Machine Learning ? """,justify=LEFT,padx =20).pack()
Radiobutton(root, text = "The autonomous acquisition of knowledge through the use of computer programs", variable = var, value = 1, command = sel).pack( anchor = W )
Radiobutton(root, text = "The autonomous acquisition of knowledge through the use of manual programs", variable = var, value = 2,command = sel).pack( anchor = W )
Radiobutton(root, text = "The selective acquisition of knowledge through the use of computer programs", variable = var, value = 3,command = sel).pack( anchor = W)
Radiobutton(root, text = "The selective acquisition of knowledge through the use of computer programs", variable = var, value = 4,command = sel).pack( anchor = W)

label = Label()
label.pack()

Label(root,text=""" What's Machine Learning ? """,justify=LEFT,padx =20).pack()
R1 = Radiobutton(root, text = "The autonomous acquisition of knowledge through the use of computer programs", variable = var, value = 5, command = sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text = "The autonomous acquisition of knowledge through the use of manual programs", variable = var, value = 6,command = sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text = "The selective acquisition of knowledge through the use of computer programs", variable = var, value = 7,command = sel)
R3.pack( anchor = W)

R4 = Radiobutton(root, text = "The selective acquisition of knowledge through the use of computer programs", variable = var, value = 8,command = sel)
R4.pack( anchor = W)

label = Label()
label.pack()
root.mainloop()


