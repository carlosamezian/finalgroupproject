##WORK IN PROGRESS
import random
import csv

class GroupManage:
    """Adds and drops users in CSV file
    Attributes:
    None
    """
    def __init__(self):
        self.filename = "user.csv"
        with open (self.filename, 'w') as self.writecsv:
            self.columns = ['First Name', 'Last Name', 'Email']
            self.writer = csv.DictWriter(self.writecsv, fieldnames=self.columns)
            self.writer.writeheader()
        self.appcsv = open(self.filename, 'a', newline='')
        self.readcsv = open(self.filename, 'r')
        self.user = {}
        self.lis = []
        self.li = []

    def add_user(self):
        """Adds user to CSV file
        Args:
        None
        
        Returns:
        None
        """
        for row in self.readcsv.readlines():
            self.li.append(row)
        firstname = input("first name: ")
        for i in firstname:
            while i.isnumeric():
                firstname = input("type in real name: ")
                for i in firstname:
                    if i.isnumeric() == False:
                        continue
            
        lastname = input("last name: ")
        for i in lastname:
            while i.isnumeric():
                lastname = input("type in real name: ")
                for i in lastname:
                    if i.isnumeric() == False:
                        continue

        email = input("email: ")
        self.lis = [firstname, lastname, email]
        for i in self.lis:
            if i not in self.li:
                self.li.append(i,'\n')
        self.app = csv.writer(self.appcsv)
        self.app.writerow(self.lis)
        self.appcsv.close()

    def drop_user(self):
        """Drops user from CSV file
        Args:
        Nones
        
        Returns:
        None
        """
        #lines = []
        #self.read = csv.reader(self.readcsv)
        for row in self.readcsv.readlines():
            print(row)
        #self.readcsv.close()
        #user = input('Drop user: ')
        #reader = csv.reader(self.readcsv)
        #for row in reader:
            #lines.append(row)
            #for field in row:
                #if field == user:
                    #lines.remove(row)
        #writer = csv.writer(self.writecsv)
        #writer.writerows(lines)
        


if __name__ == '__main__':
    group = GroupManage()
    group.add_user()
    group.drop_user()


