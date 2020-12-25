from tkinter import *
import psutil
import time


def center():
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))


while (True):
    time.sleep(1)
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    percentInStr = str(percent)+str("%")

    if percent <= 20 and plugged == False:
        root = Tk()
        center()
        lable1 = Label(root, text=percentInStr)
        lable2 = Label(root, text="Battery is getting Low")
        lable3 = Label(root, text="Please Plug in the Charger.")
        lable1.pack()
        lable2.pack()
        lable3.pack()
        root.after(3000, lambda: root.destroy())
        root.mainloop()
        time.sleep(300)

    if percent >= 90 and plugged == True:
        root = Tk()
        center()
        lable5 = Label(root, text="Battery is on "+percentInStr)
        lable8 = Label(root, text="Please Un-Plug the Charger.")
        lable5.pack()
        lable8.pack()
        root.after(3000, lambda: root.destroy())
        root.mainloop()
        time.sleep(30)
