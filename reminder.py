import time
from win10toast import ToastNotifier
import tkinter as tk


class Remind:

    def __init__(self, text, time):
        """The attributes that class will hold.
        Args:
            text (string): the reminder that the user states.
            time (int): the time it takes for the reminder to pop up
        """
        self.text = text
        self.mytime = time

    def notif(self):
        """This method will contril the notifications. It will wait that specifiied time before printing the
        notification. It will display it and make a sound.
        
        Args:
            None
        """
        mynotif = ToastNotifier()
        mynotif.show_toast("Reminder:", "Will go off in {} min(s) ".format(
            self.mytime), duration=10)
        time.sleep(self.mytime * 60)
        mynotif.show_toast("Reminder: {}".format(self.text), duration=10)

def create(text, time):
    floatTime=float(time)
    myremind = Remind(text, floatTime)
    myremind.notif()
    root=tk.Tk()
    label1=tk.Label(root, text= "Reminder has been set. you may close the previous window or create a new reminder")
    label1.pack()
    
def main():
    """The main function to ask the user for reminder and time.
    """
    
    root=tk.Tk()
    entry1=tk.Entry(root, text="What would you like to be reiminded about? ", width=35)
    entry1.grid(row=0, column=0)
    entry2=tk.Entry(root, text="In how long?(minutes)", width=35)
    entry2.grid(row=1, column=0)
    button1=tk.Button(root, text= "Create", command=lambda: create(entry1.get(),entry2.get()))
    button1.grid(row=3, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()