import groupmanage as gm
import appointment
import reminder
import tkinter as tk



root=tk.Tk()

button1=tk.Button(root, text= "Group Management", command=gm.menu())
button1.grid(row=0)

button2=tk.Button(root, text= "Appointments", command=appointment.main())
button2.grid(row=1)

button3=tk.Button(root, text= "Reminders", command=reminder.main())
button3.grid(row=2)


root.mainloop()