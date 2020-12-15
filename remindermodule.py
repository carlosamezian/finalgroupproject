import time
from win10toast import ToastNotifier


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


def main():
    """The main function to ask the user for reminder and time.
    """
    text = input("What would you like to be reiminded about? ")
    time = float(input("In how long?(minutes)"))

    myremind = Remind(text, time)

    myremind.notif()


if __name__ == "__main__":
    """Main functuon.
    """
    main()
