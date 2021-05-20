import time
from plyer import notification

if __name__ =='__main__':
    while True:
        notification.notify(


        title="Nishan Please Drink water now",
        message="The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men.",
        app_icon="/home/nishan/Documents/Drinkig Water Project/icon.ico",
        timeout=5
)
        time.sleep(60*30)
