import time
import datetime
from plyer import notification
import pyttsx3



engine = pyttsx3.init()
engine.setProperty("rate",100)
engine.setProperty("volume",1)#full volume 1 or 0 for minimal volume
voice = engine.getProperty('voices')
engine.setProperty("voice", voice[1].id)#0 for male 1 for female 


def checkNotification():
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        date = current_time.strftime("%m/%d/%y")
        now = current_time.strftime("%I:%M:%S %p")
        fileName = open("C:\\Notifier\\data.csv","r")
        for line in fileName: 
            line = line.split(',')
            #print(line[1]," ",now)
            if date==line[0] and now==line[1]:
                notification.notify(
                title="Notification that you set",
                message=line[2],
                app_name="Notifier",
                #app_icon="reminder.ico",
                timeout=50 
                )
                engine.say(line[2])
                engine.runAndWait()
                





        """with open('data.csv', 'r')as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if date==line[0] and now==line[1]:
                    notification.notify(
                    title="Notification that you set",
                    message=line[2],
                    app_name="Notifier",
                    #app_icon="C:\Alarm Clock Using Python With Source Code\reminder.ico",
                    timeout=50
                    ) 
                    engine.say(line[2])
                    engine.runAndWait()
                """
                #break

   
if __name__ == '__main__':
    checkNotification()

