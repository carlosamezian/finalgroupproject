##WORK IN PROGRESS
import random
import csv
import os.path

class GroupManage:
    def __init__(self):
        self.filename = "user.csv"
        exists = os.path.isfile(self.filename)
        with open (self.filename, 'a') as self.appcsv:
            self.headers = ['First Name', 'Last Name', 'Email']
            self.writer = csv.DictWriter(self.appcsv, fieldnames=self.headers)
            if not exists:
                self.writer.writeheader()
        self.user = {}
        self.lis = []
        

    def add_user(self):
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
        with open(self.filename, 'a') as self.appcsv:
            self.app = csv.writer(self.appcsv)
            self.app.writerow(self.lis)

    def drop_user(self):
        #lines = []
        user = input('Drop user: ')
        with open (self.filename, 'r') as self.readcsv:
            for row in self.readcsv.readlines():
                 print(row)
                 if user in row:
                     filename.remove(user)
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
    #group.add_user()
    group.drop_user()


