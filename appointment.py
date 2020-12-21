# Module Coder: Miguel Mayo
# Class: INST 326
# Instructor: Prof Cruz
# Due Date: 12/21/2020
# Code Updated on: 12/20/2020

"""Appointment scheduler Module

This module will create a Gui for the user to view, create, and delete their appointments
"""

import re
import sys
import datetime
import tkinter as tk


# This is the main object the module will be dealing with
class appointment:
    
    def __init__(self, name, start_datetime, end_datetime):
        
        self.name=name
        self.start_datetime=start_datetime
        self.end_datetime=end_datetime
        
    def save(self):
        
        """This method saves the objects data by writing it to a text file
        
        Side Effects: Appends schedule.txt file
        """
        fh=open("schedule.txt", "a")
        fh.write(self.name+" ")
        fh.write(self.start_datetime.strftime("%c")+" ")
        fh.write(self.end_datetime.strftime("%X")+'\n')
        fh.close
    
    def overlaps(self, Schedule):
        
        """Checks to see if a new appointment will overlap with any in the schedule
        
        Args: Schedule(list): list of appointment objects
        
        Returns: (Boolean): Will return the boolean value that corresponds with whether there is an overlap or not.
        """
        #Check to see if list is empty
        if len(Schedule)==0:
            return False
        else:
            # Start by checking if the two are on the same day
            for appointment in Schedule:
                date1=self.start_datetime.strftime("%x")
                date2=appointment.start_datetime.strftime("%x")
                if date1== date2:
                
                    # Created simple variables to store start and end times 
                    a=self.start_datetime.strftime("%X")
                    b=self.end_datetime.strftime("%X")
                    c=appointment.start_datetime.strftime("%X")
                    d=appointment.end_datetime.strftime("%X")
        
                    # First set of statements check the other appointment against the first
                    # Checks to see if the start of other occurs between a and b
                    if a<c and c<b:
                        return True
                    # Checks to see if the end of other occurs between a and b
                    elif a<d and d<b:
                        return True
        
                    # Second set of statements check the first appointment against the other
                    # Checks to see if the start of first appointment occurs between c and d
                    elif c<a and a<d: 
                        return True 
                    # Checks to see if the end of first appointment occurs between c and d
                    elif c<b and b<d:
                        return True
                    # This outcome should only occur if there is no overlap
                    else:
                        return False
                # This outcome occurs when the two objects have different dates
                else:
                    return False

# GUI functions:
def view_appointments():
    """ Opens the schedule.txt file, and visually displays saved appointments 
    
    Side Effects: GUI screen will pop up
    """
    # Create the GUI
    # Start with the functions screen
    # Create root screen
    root=tk.Tk(screenName=None,  baseName=None,  className='Schedule',  useTk=1)
    
    # Format the GUI
    # Column 1
    label1=tk.Label(root, text="Appointments: ")
    label1.grid(row=0, column=0, columnspan=2)
    # Empty label purely aesthetic
    labelEmpty=tk.Label(root, text=" ")
    labelEmpty.grid(row=1,column=0)
    # Column 2
    label2=tk.Label(root, text="Name: ")
    label2.grid(row=2, column=0)
    textName=tk.Text(root, width=35)
    textName.grid(row=3, column=0)
    # Column 3
    label3=tk.Label(root, text="Date: ")
    label3.grid(row=2, column=1)
    textDate= tk.Text(root, width=11) 
    textDate.grid(row=3,column=1)
    # Column 4
    label4=tk.Label(root, text="Start: ")
    label4.grid(row=2, column=2)
    textStart= tk.Text(root, width=8) 
    textStart.grid(row=3,column=2)
    # Column 5
    label5=tk.Label(root, text="End: ")
    label5.grid(row=2, column=3)
    textEnd= tk.Text(root, width=8) 
    textEnd.grid(row=3,column=3)
    
    # Extract the data and insert it into GUI
    fh=open("schedule.txt",'r')
    for line in fh:
        
        subject=str(line)
        
        # Name 
        patternName= r'^(.*)[MTWFS]\w\w'
        regex=re.compile(patternName)
        Name=regex.findall(subject)
        textName.insert('end', Name[0])
        textName.insert('end', '\n')
        
        # Date
        patternDate= r'([A-Z]\w\w\s\d\d)'
        regex=re.compile(patternDate)
        Date=regex.findall(subject)
        textDate.insert('end', Date[0])
        textDate.insert('end', " ")
        patternYear= r'\:\d\d\s(\d{4})'
        regex=re.compile(patternYear)
        Year=regex.findall(subject)
        textDate.insert('end',Year[0])
        textDate.insert('end', '\n')
        
        # Start
        patternStart= r'(\d*\:\d*\:\d*)\s\d{4}'
        regex=re.compile(patternStart)
        Start=regex.findall(subject)
        textStart.insert('end',Start[0])
        textStart.insert('end', '\n')
        
        # End
        patternEnd= r'\d{4}\s(\d*\:\d*\:\d*)'
        regex=re.compile(patternEnd)
        End=regex.findall(subject)
        textEnd.insert('end', End[0])
        textEnd.insert('end', '\n')
    fh.close
        
def create(Name, Start, End):
    
    """Creates an appointment object using the parameters passed
    
    Args: Name(str): name of the appointment, Start(datetime object): start time of
    the appointment, End(datetime object): end time of the appointment.
    
    Side Effects: Will create pop up tp let user know if there was an error or not. Will not
    save if there is an overlap. Appends shcedule.txt.
    """
          
    
    # Create new appointment
    newAppointment=appointment(Name,Start,End)
    # Create list of old Appointments
    # Start by opening text of saved appointments and iterate through
    fh=open("schedule.txt",'r')
    list1=[]
    for line in fh:
        subject=str(line)
        
        # Name 
        patternName= r'^(.*)[MTWFS]\w\w'
        regex=re.compile(patternName)
        match=regex.findall(subject)
        Name=match[0]
        
        # Start time
        patternYear=r'00\s(\d{4})\s\d\d'
        regex=re.compile(patternYear)
        match=regex.findall(subject)
        Year=int(match[0])
        patternMonth=r'[MTWFS]\w\w\s([A-Z]\w\w)\s\d'
        regex=re.compile(patternMonth)
        match=regex.findall(subject)
        MonthStr=match[0]
        if MonthStr=="Jan":
            MonthInt=1
        if MonthStr=="Feb":
            MonthInt=2
        if MonthStr=="Mar":
            MonthInt=3
        if MonthStr=="Apr":
            MonthInt=4
        if MonthStr=="May":
            MonthInt=5
        if MonthStr=="Jun":
            MonthInt=6
        if MonthStr=="Jul":
            MonthInt=7
        if MonthStr=="Aug":
            MonthInt=8
        if MonthStr=="Sep":
            MonthInt=9
        if MonthStr=="Oct":
            MonthInt=10
        if MonthStr=="Nov":
            MonthInt=11
        if MonthStr=="Dec":
            MonthInt=12
        patternDay=r'[A-Z]\w\w\s(\d+)'
        regex=re.compile(patternDay)
        match=regex.findall(subject)
        Day=int(match[0])
        patternHour=r'[A-Z]\w\w\s\d+\s(\d+)\:'
        regex=re.compile(patternHour)
        match=regex.findall(subject)
        Hour=int(match[0])
        patternMinute=r'[A-Z]\w\w\s\d+\s(\d+)\:'
        regex=re.compile(patternMinute)
        match=regex.findall(subject)
        Minute=int(match[0])
        
        Start=datetime.datetime(Year, MonthInt, Day, Hour, Minute)
        
        patternHour=r'\d{4}\s(\d+)\:'
        regex=re.compile(patternHour)
        match=regex.findall(subject)
        Hour=int(match[0])
        patternMinute=r'\d{4}\s\d+\:(\d+)\:'
        regex=re.compile(patternMinute)
        match=regex.findall(subject)
        Minute=int(match[0])
    
        End=datetime.datetime(Year, MonthInt, Day, Hour, Minute)
        scheduledAppointment=appointment(Name,Start,End)
        list1.append(scheduledAppointment)
    
    fh.close
    if newAppointment.overlaps(list1)==False:
        newAppointment.save()
        root=tk.Tk()
        label1=tk.Label(root, text="Success! You may close the previous screen or create another appointment")
        label1.pack()
    else:
        root=tk.Tk()
        label1=tk.Label(root, text="Appointment overlaps with a previous appointment. Close this screen and try again")
        label1.pack()
        
     
def create_appointment():
    
    """Allows the user to create a new appointment object by entering in its meta data
    
    Side Effects: Creates a new pop up window, and will append schedule.txt file
    """
    
    #Root Screen
    root=tk.Tk(screenName=None,  baseName=None,  className='Create an Appointment',  useTk=1)
    
    
    # Name row
    tk.Label(root, text='Name').grid(row=0) 
    entry1 = tk.Entry(root, width=35) 
    entry1.grid(row=0, column=1)
    entry1.insert("end", 'Max 35 Characters')
    
    # Date row
    tk.Label(root, text='Date').grid(row=1) 
    entry2 = tk.Entry(root, width=35)
    entry2.grid(row=1, column=1) 
    entry2.insert("end", 'Integer format (year, month, day)')

    # Start row
    tk.Label(root, text='Start Time').grid(row=2)
    entry3 = tk.Entry(root,width=35)
    entry3.grid(row=2, column=1)
    entry3.insert("end", 'Use the military time format 24:00')

    # End row
    tk.Label(root, text='End Time').grid(row=3)
    entry4 = tk.Entry(root,width=35)
    entry4.grid(row=3, column=1)
    entry4.insert("end", 'Use the military time format 24:00')
    
    
    placeholder=tk.Label(root, text=" ")
    placeholder.grid(row=5,column=1)
    myButton=tk.Button(root, text="Create", command=lambda: extract(str(entry1.get()),str(entry2.get()),str(entry3.get()),str(entry4.get())))
    myButton.grid(row=6, column=1)

def extract(subject1, subject2, subject3, subject4 ):
    """Extracts the metadata from lines of string
    
    Args: subject1(str):entry1.get data, subject2(str):entry2.get data,
    subject3(str):entry3.get data, subject4(str):entry4.get data
    """
    
    Name=subject1
    Date=subject2
    # Extract the variables to pass to create function
    
    subject=Date
    
    patternYear=r'(\d{4})'
    regex=re.compile(patternYear)
    match=regex.findall(subject)
    Year=int(match[0])
    
    patternMonth=r'\d{4}\,\s?(\d+)\,'
    regex=re.compile(patternMonth)
    match=regex.findall(subject)
    Month=int(match[0])
    
    patternDay=r'\d+\,\s?\d+\,\s?(\d+)'
    regex=re.compile(patternDay)
    match=regex.findall(subject)
    Day=int(match[0])
    
    startTime=subject3
    subject=startTime
    
    patternHour=r'^([1-2]?\d+)\:'
    regex=re.compile(patternHour)
    match=regex.findall(subject)
    startHour=int(match[0])
    
    patternMinute=r'\:0?(\d+)'
    regex=re.compile(patternMinute)
    match=regex.findall(subject)
    startMinute=int(match[0])
    
    endTime=subject4
    subject=endTime
    
    patternHour=r'^([1-2]?\d+)\:'
    regex=re.compile(patternHour)
    match=regex.findall(subject)
    endHour=int(match[0])
    
    patternMinute=r'\:0?(\d+)'
    regex=re.compile(patternMinute)
    match=regex.findall(subject)
    endMinute=int(match[0])
    
    Start=datetime.datetime(Year, Month, Day, startHour, startMinute)
    End=datetime.datetime(Year, Month, Day, endHour, endMinute)
    
    create(Name,Start,End)
 
def delete_appointment():
    
    """Allows user to delete an appointment by identifying it by name
    
    Side effects: Creates pop up windows and calls search().
    """
    root=tk.Tk()
    label1=tk.Label(root,text="Name: ")
    label1.grid(row=0, column=0)
    entry1=tk.Entry(root, text="Type Appointment Name Here", width=35)
    entry1.grid(row=0, column=1)
    # Create list of old Appointments
    # Start by opening text of saved appointments and iterate through
    fh=open("schedule.txt",'r')
    list1=[]
    for line in fh:
        subject=str(line)
        
        # Name 
        patternName= r'^(.*)[MTWFS]\w\w'
        regex=re.compile(patternName)
        match=regex.findall(subject)
        Name=match[0]
        
        # Start time
        patternYear=r'00\s(\d{4})\s\d\d'
        regex=re.compile(patternYear)
        match=regex.findall(subject)
        Year=int(match[0])
        patternMonth=r'[MTWFS]\w\w\s([A-Z]\w\w)\s\d'
        regex=re.compile(patternMonth)
        match=regex.findall(subject)
        MonthStr=match[0]
        if MonthStr=="Jan":
            MonthInt=1
        if MonthStr=="Feb":
            MonthInt=2
        if MonthStr=="Mar":
            MonthInt=3
        if MonthStr=="Apr":
            MonthInt=4
        if MonthStr=="May":
            MonthInt=5
        if MonthStr=="Jun":
            MonthInt=6
        if MonthStr=="Jul":
            MonthInt=7
        if MonthStr=="Aug":
            MonthInt=8
        if MonthStr=="Sep":
            MonthInt=9
        if MonthStr=="Oct":
            MonthInt=10
        if MonthStr=="Nov":
            MonthInt=11
        if MonthStr=="Dec":
            MonthInt=12
        patternDay=r'[A-Z]\w\w\s(\d+)'
        regex=re.compile(patternDay)
        match=regex.findall(subject)
        Day=int(match[0])
        patternHour=r'[A-Z]\w\w\s\d+\s(\d+)\:'
        regex=re.compile(patternHour)
        match=regex.findall(subject)
        Hour=int(match[0])
        patternMinute=r'[A-Z]\w\w\s\d+\s(\d+)\:'
        regex=re.compile(patternMinute)
        match=regex.findall(subject)
        Minute=int(match[0])
        
        Start=datetime.datetime(Year, MonthInt, Day, Hour, Minute)
        
        patternHour=r'\d{4}\s(\d+)\:'
        regex=re.compile(patternHour)
        match=regex.findall(subject)
        Hour=int(match[0])
        patternMinute=r'\d{4}\s\d+\:(\d+)\:'
        regex=re.compile(patternMinute)
        match=regex.findall(subject)
        Minute=int(match[0])
    
        End=datetime.datetime(Year, MonthInt, Day, Hour, Minute)
        scheduledAppointment=appointment(Name,Start,End)
        list1.append(scheduledAppointment)
    fh.close
    button1=tk.Button(root, text="Search", command=lambda: search(list1,str(entry1.get())))
    button1.grid(row=1,column=0)

def search(list1, searchName):
    
    """Searches a list for an appointment object with a .name attribute that matches searchName
    
    Args: list1(list): list of appointment objects, searchName(str):string containing name to search for
    
    Side Effects: Creates more pop up windows. If a match is found, it calls delete() and gives it the name
    """
    if len(list1)==0:
        root=tk.Tk()
        label1=tk.Label(root,text="No match found v1")
        label1.grid(row=0, column=0)
    found=False
    counter=0
    while found== False: 
        if counter== len(list1):
            root=tk.Tk()
            label1=tk.Label(root,text="No match found v2")
            label1.grid(row=0, column=0)
            found=True
        elif list1[counter].name[:-1]== searchName:
            root=tk.Tk()
            label1=tk.Label(root,text=list1[counter].name)
            label1.grid(row=0, column=0)
            button1=tk.Button(root, text="DELETE This Appointment?", command= lambda: delete(list1[counter].name))
            button1.grid(row=1,column=0)
            found=True  
        else:
            counter+=1
    
def delete(deleteName):
    
    """Deletes the appointment from the text file
    
    Args: deleteName(str); the name of the appointment to be deleted
    
    Side Effects: Alters schedule.txt
    """
    
    root=tk.Tk()
    label1=tk.Label(root, text= "Appointment has been delated. You can close the last window or delete another")
    label1.pack()
    with open("schedule.txt", "r") as f:
        lines = f.readlines()
    with open("schedule.txt", "w") as f:
        for line in lines:
            if line.startswith(deleteName):
                pass
            else:
                f.write(line)
        
    

def main():
    # Create the GUI root menu
    root = tk.Tk() 
    frame1=tk.Frame(root)
    frame1.pack()


    # Create a text file for storing appointments
    fh=open('schedule.txt','a')
    fh.close

    # Create the GUI buttons

    # Appointments Menu Button 1  
    button1=tk.Button(frame1, text="View Appointments", command=view_appointments)
    button1.grid(row=0, column=0)

    # Appointments Menu Button 2
    button2=tk.Button(frame1, text="Create Appointment", command=create_appointment)
    button2.grid(row=1, column=0)

    # Appointments Menu Button 3
    button3=tk.Button(frame1, text="Delete Appointment", command=delete_appointment)
    button3.grid(row=2, column=0)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
    
    
    
    
