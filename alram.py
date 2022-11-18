from datetime import datetime
import time
import threading

class Alarm:

    def __init__(self,alarm_time:datetime) -> None:
        self.current_time = datetime.now()
        self.alarm_time = alarm_time
        self.alarm_duration = 1000 # sec
        self.ringing_threads = None
        self._ring()
        
    def _ring(self):
        
        if self.current_time == self.alarm_time:
            count = 0
            while count<=self.alarm_duration:
                print("Alram rining")
                # time.sleep(self.alarm_duration)
                # break
                count+=1



class AlramManager:

    def __init__(self):
        self.current_time = datetime.now()
        self.alarms = []
    
    def add_alram(self,time,day):
        # time: hr:min:sec
        # day:mon-sun
        alarm_time = datetime.now()
        alarm = threading.Thread(target=)
        self.alarms.append(Alarm(alarm_time=alarm_time))

    def snooze_alarm(self):
        # snooze alarm  upto 3 times interval of 5 min each
        pass

    def delete_alram(self):
        # delete an alarm
        self.alrams.pop()