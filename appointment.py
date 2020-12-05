import re
import tkinter as tk
from functools import partial
  
root = tk.Tk() 
frame1=tk.Frame(root)
frame1.pack()

# Create a text file for storing appointments
fh=open('schedule.txt','a')
fh.close

class appointment:
    
    def __init__(self, ID, name, date, time):
        
        self.ID=ID
        self.name=name
        self.date=date
        self.time=time
    

def click1():
    
    root=tk.Tk(screenName=None,  baseName=None,  className='Schedule',  useTk=1)
    
    label1=tk.Label(root, text="Appointments: ")
    label1.grid(row=0, column=0)
    
    labelEmpty=tk.Label(root, text=" ")
    labelEmpty.grid(row=1,column=0)
    
    label2=tk.Label(root, text="ID#: ")
    label2.grid(row=2, column=0)
    textID=tk.Text(root, width=3)
    textID.grid(row=3, column=0)
    
    label3=tk.Label(root, text="Name: ")
    label3.grid(row=2, column=1)
    textName= tk.Text(root, width=30) 
    textName.grid(row=3,column=1)
    
    label4=tk.Label(root, text="Date: ")
    label4.grid(row=2, column=2)
    textDate= tk.Text(root, width=10) 
    textDate.grid(row=3,column=2)
    
    label5=tk.Label(root, text="Time: ")
    label5.grid(row=2, column=3)
    textTime= tk.Text(root, width=8) 
    textTime.grid(row=3,column=3)
    
    fh=open('schedule.txt')
    for line in fh:
        subject=str(line)
        
        patternID= r'^(\d*)'
        regex=re.compile(patternID)
        ID=regex.findall(subject)
        textID.insert('end', ID[0])
        textID.insert('end', '\n')
        
        patternName= r'\d\s(.*)\s\d*\/'
        regex=re.compile(patternName)
        name=regex.findall(subject)
        textName.insert('end', name[0])
        textName.insert('end', '\n')
        
        patternDate= r'(\d*\/\d*\/\d*)'
        regex=re.compile(patternDate)
        date=regex.findall(subject)
        textDate.insert('end', date[0])
        
        patternTime= r'(\d*\:\d*\s\w\w)'
        regex=re.compile(patternTime)
        time=regex.findall(subject)
        textTime.insert('end', time[0])
         
    fh.close
    
    root.mainloop()
    
def click2():
    
    root=tk.Tk(screenName=None,  baseName=None,  className='Create an Appointment',  useTk=1)
    
    tk.Label(root, text='Name').grid(row=0) 
    tk.Label(root, text='Date').grid(row=1) 
    tk.Label(root, text='Time').grid(row=2)
    entry1 = tk.Entry(root) 
    entry2 = tk.Entry(root) 
    entry3 = tk.Entry(root)
    entry1.grid(row=0, column=1) 
    entry2.grid(row=1, column=1) 
    entry3.grid(row=2, column=1)
    
    name=entry1.get
    name=str(name)
    date=entry2.get
    date=str(date)
    time=entry3.get
    time=str(time)
    myButton=tk.Button(root, text="Create", command=partial(create, name, date, time))
    myButton.grid(row=3)
    root.mainloop() 
    
def create(name,date,time):

    fh=open('schedule.txt','r')
    counter=0
    for line in fh:
        counter+=1
    fh.close
    ID=counter+1
    ID=str(ID)
    fh=open('schedule.txt','a')
    fh.write(ID)
    fh.write(name)
    fh.write(date)
    fh.write(time)
    
    
button1=tk.Button(frame1, text="View Appointments", command=click1)
button1.grid(row=0, column=0)

button2=tk.Button(frame1, text="Create Appointment", command=click2)
button2.grid(row=1, column=0)

button3=tk.Button(frame1, text="Delete Appointment")
button3.grid(row=2, column=0)

button4=tk.Button(frame1, text="Return to Main Menu")
button4.grid(row=3, column=0)

root.mainloop()