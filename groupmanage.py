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
        
    def add_user(self):
        """Adds a user to CSV file
        
        Args:
        filename (string): The name of the file
        readcsv: Reads the CSV file
        lis (list): List of user information
        app: Appends user information to CSV file
        appcsv: Variable for appending to CSV file
        
        Returns: None
        """
        name = input("Enter full name: ") # User's name
        for i in name: # Error handling for name
            while i.isnumeric():
                name = input("Type in a valid name: ")
                for i in name:
                    if i.isnumeric() == False:
                        continue
        
        email = input("Enter email address: ") # User's email address
        while re.search('[\w\d.-_]+\.\w+', email) == None: # Error handling for email address syntax
            email = input("Enter a valid email address: ")
        userlist = [] # List of user information in each row
        with open (self.filename, 'r') as self.readcsv: # Converts CSV rows to a list to check if the inputted email address is in the list
            reader = csv.reader(self.readcsv)
            for row in reader:
                userlist.append(row)
                for field in row:
                    while email in row:
                        email = input("Email address already taken! Enter another email address: ")
        
        password = random.randint(1000000000,9999999999) # Random 10 digit password for user
            
        self.lis = [name, email, password] # List of user information

        with open(self.filename, 'a', newline='') as self.appcsv: # Appending user information to CSV file
            self.app = csv.writer(self.appcsv)
            self.app.writerow(self.lis)

    def drop_user(self):
        """Drops a user from CSV file

        Args:
        filename (string): The name of the file
        readcsv: Variable for reading CSV file
        writecsv: Variable for writing to CSV file


        Returns: None
        """
        userlist = [] # List of user information in each row
        user = input('Email of user to remove: ') # User to be removed
        while re.search('[\w\d.-_]+\.\w+', user) == None: # Error handling for email address
            user = input("Type in an email address: ")
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
