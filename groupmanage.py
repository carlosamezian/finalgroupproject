import random
import csv
import os.path
import re
import tkinter as tk


class GroupManage:
    """Class for adding and removing users from a CSV file
    Attributes: None
    """
    def __init__(self):
        """
        Args:
        filename (string): The name of the file
        lis (list): List of user information
        exists (boolean): Bool for checking 'existence' within the file path
        appcsv: Variable for appending to CSV file
        headers (list): CSV file header names
        writer: Uses Dictwriter function from CSV module
        """
        self.filename = "user.csv" # Name of the file
        self.lis = [] # List of user information
        self.exists = os.path.isfile(self.filename) # Bool for checking 'existence' within the file path

        with open (self.filename, 'a') as self.appcsv: # Opening CSV file to append to it
            self.headers = ['Name', 'Email', 'Password'] # CSV file header names
            self.writer = csv.DictWriter(self.appcsv, fieldnames=self.headers)
            if not self.exists:
                self.writer.writeheader() # Writes header names in CSV file if they aren't already there
        
    def add_user(self, name, email):
        """Sets up user info for GUI
        
        Args:
        filename (string): The name of the file
        lis (list): List of user information
        app: Appends user information to CSV file
        appcsv: Variable for appending to CSV file
        
        Returns: None
        """
        
        password = random.randint(1000000000,9999999999) # Random 10 digit password for user
            
        self.lis = [name, email, password] # List of user information

        with open(self.filename, 'a', newline='') as self.appcsv: # Appending user information to CSV file
            self.app = csv.writer(self.appcsv)
            self.app.writerow(self.lis)
        
        root=tk.Tk()
        label1=tk.Label(root, text="Success you may close the previous window or type in a new user")
        label1.pack()

    def drop_user(self, user):
        """Sets up user drop for GUI
        Args:
        filename (string): The name of the file
        readcsv: Variable for reading CSV file
        writecsv: Variable for writing to CSV file

        Returns: None
        """
        userlist = [] # List of user information in each row
        with open (self.filename, 'r') as self.readcsv: # Converts CSV rows to a list and removes inputted user information from list
            reader = csv.reader(self.readcsv)
            for row in reader:
                userlist.append(row)
                for field in row:
                    if field == user:
                        userlist.remove(row)
        with open (self.filename, 'w') as self.writecsv: # Overwrites original CSV file to update it
            writer = csv.writer(self.writecsv)
            writer.writerows(userlist)
        root=tk.Tk()
        label1=tk.Label(root, text="Success you may close previous window or type another user")
        label1.pack()
        
if __name__ == '__main__':
    myGroup=GroupManage()

    root=tk.Tk()

    label1=tk.Label(root, text= "Enter User Info Below (Case Sensitive): ")
    label1.grid(row=0,column=0)

    entry1=tk.Entry(root, width=35) 
    entry1.grid(row=1, column=1)
    entry1.insert("end", 'Student Name Here')

    entry2=tk.Entry(root, width=35) 
    entry2.grid(row=2, column=1)
    entry2.insert("end", 'Student Email Here')

    Add_User_Button=tk.Button(root, text="Add User", command= lambda: myGroup.add_user(entry1.get(),entry2.get()))
    Add_User_Button.grid(row=3,column=0)

    Drop_User_Button=tk.Button(root, text="Drop User",command= lambda: myGroup.drop_user(entry2.get()))
    Drop_User_Button.grid(row=3,column=1)

    root.mainloop()
