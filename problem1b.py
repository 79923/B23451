# Import Module 
from tkinter import * 
import pandas as pd  
		
a=pd.read_excel("Defused12.xlsx")
itis = a.keys()
for ele in itis:
	print(ele)

# create root window 
root = Tk()

# root window title and dimension 
root.title("Enter Your Data...The Much You Want >>> Then click submit")

# Set geometry(width x height) 
root.geometry('350x2000') 

# adding a label to the root window 
lbl = Label(root, text = "name") 
lbl.grid() 
# creating a entry widget object 
name=Entry(root,width=20)
name.grid()

# adding a label to the root window 
lbl = Label(root, text = "Age") 
lbl.grid() 
# creating a entry widget object 
Age=Entry(root,width=20)
Age.grid()

# adding a label to the root window 
lbl = Label(root, text = "Gender") 
lbl.grid() 
# creating a entry widget object 
Gender=Entry(root,width=20)
Gender.grid()

# adding a label to the root window 
lbl = Label(root, text = "Hobby1") 
lbl.grid() 
# creating a entry widget object 
Hobby1=Entry(root,width=20)
Hobby1.grid()

# adding a label to the root window 
lbl = Label(root, text = "Hobby2") 
lbl.grid() 
# creating a entry widget object 
Hobby2=Entry(root,width=20)
Hobby2.grid()

# adding a label to the root window 
lbl = Label(root, text = "MBTI") 
lbl.grid() 
# creating a entry widget object 
MBTI=Entry(root,width=20)
MBTI.grid()

lbl = Label(root, text = "State") 
lbl.grid() 
# creating a entry widget object 
State=Entry(root,width=20)
State.grid()


btn=Button(root, text="Submit", command=thf)
btn.grid()
for i in range(300):
	lbl = Label(root, text = a["Name"][i]+"  "+str(a["Age"][i])\
	+"  "+a["Gender"][i]+"  "+a["Hobby1"][i]+"  "+a["Hobby2"][i]+"  "+a["State"][i]) 
	lbl.grid()

# Execute Tkinter
root.mainloop()









