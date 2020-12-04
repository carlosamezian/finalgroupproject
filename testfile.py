import time

class Reminder():
    
    def __init__(self, task, thetime, duedate):
        self.task = task
        self.thetime = thetime
        self.duedate = duedate
        # self.freqreminder = freqreminder

    def set_frequency(self):
        pass
    
def main(ran):
    
    print("What shall I remind you about?")
    text = str(input())

    
    if text not in ran:
        print("Task not found!")
    else:
        print("How many min from now?")
        rem = float(input())
        rem  = rem * 60
        print("You'll be reminded in {} min".format(rem))
        time.sleep(rem)
        print()

        
if __name__ == "__main__":
        
    tasks = []
    numtasks = int(input("How many tasks?"))
    
    count = 0
    while count <= numtasks:
        task = input("Whats the task needed to be done?")
        thetime = input("What time is it due?(00:00) ")
        duedate = input("Whats the due date?(MM/DD/YYYY)")
        
        mytask = Reminder(task, thetime, duedate)
        tasks.append((mytask.task, mytask.thetime, mytask.duedate))
        count = count + 1

    # print(tasks)
    main(tasks)