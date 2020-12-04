##WORK IN PROGRESS
import random
import csv
import os.path
import re

class GroupManage:
    """Class for adding and removing users from a CSV file

    Attributes: None

    """
    def __init__(self):
        """
        Args:
        filename (string) : Name of the file
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
            self.headers = ['First Name', 'Last Name', 'Email'] # CSV file header names
            self.writer = csv.DictWriter(self.appcsv, fieldnames=self.headers)
            if not self.exists:
                self.writer.writeheader() #Writes header names in CSV file if they aren't already there
        
    def add_user(self):
        """Adds a user to CSV file
        
        Args: None
        
        Returns: None
        """
        firstname = input("Enter first name: ") # User's first name
        for i in firstname: # Error handling for first name
            while i.isnumeric():
                firstname = input("Type in a valid name: ")
                for i in firstname:
                    if i.isnumeric() == False:
                        continue
            
        lastname = input("Enter last name: ") # User's last name
        for i in lastname: # Error handling for last name
            while i.isnumeric():
                lastname = input("Type in a valid name: ")
                for i in lastname:
                    if i.isnumeric() == False:
                        continue
        
        email = input("Enter email address: ") # User's email address
        while re.search('[\w\d.-_]+\.\w+', email) == None: # Error handling for email address
            email = input("Type in a valid email address: ")
            
        self.lis = [firstname, lastname, email] # List of user information
        with open(self.filename, 'a') as self.appcsv: #Appending user information to CSV file
            self.app = csv.writer(self.appcsv)
            self.app.writerow(self.lis)

    def drop_user(self):
        """Drops a user from CSV file

        Args: None

        Returns: None
        """
        userlist = [] # List of user information in each row
        user = input('Name of user to remove: ') # User to be removed
        with open (self.filename, 'r') as self.readcsv: # Converts CSV rows to a list and removes inputted user information from list
            reader = csv.reader(self.readcsv)
            for row in reader:
                userlist.append(row)
                print(row)
                for field in row:
                    if field == user:
                        userlist.remove(row)
        with open (self.filename, 'w') as self.writecsv: # Overwrites original CSV file to update it
            writer = csv.writer(self.writecsv)
            writer.writerows(userlist)
        print(userlist)

if __name__ == '__main__':
    group = GroupManage()
    choice = input("1. Add user\n2. Drop user")
    if choice == '1':
        group.add_user()
    if choice == '2':
        group.drop_user()

