import time
import winsound
from win10toast import ToastNotifier


def main():
    print("What shall I remind you about?")
    text = str(input())

    print("In how many minutes?")

    local_time = float(input())

    local_time = local_time * 60

    time.sleep(local_time)

    print(text)


def reminders(remind, time):
    notif = ToastNotifier()
    notif.show_toast("Reminder:", f""" Goes of in {time} secs""", duration=20)
    notif.show_toast(f"Reminder", remind, duration=20)

    freq = 2500
    dur = 1000
    winsound.Beep(freq, dur)


if __name__ == "__main__":
    reminders("Test", 20)
