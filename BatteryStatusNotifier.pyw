import psutil
import time
from win10toast import ToastNotifier


while (True):
    toaster = ToastNotifier()
    time.sleep(1)
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    percentInStr = str(percent)+str("%")

    if percent <= 20 and plugged == False:
        toaster.show_toast("Battery Low","Please Plug-In the Charger.",duration=10,icon_path="./battery low.ico")
        time.sleep(150)

    if percent >= 90 and plugged == True:
        toaster.show_toast("Battery Full","Please Plug-Out the Charger.",duration=10,icon_path="./battery full.ico")
        time.sleep(30)
