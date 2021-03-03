class Time:
    def __init__(self,hour,minutes):
        self.hour= hour
        self.minutes = minutes
    def addTime(self):
        time_2_hr=int(input("Enter Time in Hours"))
        time_2_min=int (input("Enter time in minutes"))
        addTimehr=self.hour+time_2_hr
        addTimemin=self.minutes+time_2_min
        if(addTimemin>=60):
            addTimehr=addTimehr+addTimemin/60
            addTimemin=addTimemin%60
            A=Time(addTimehr,addTimemin)
            A.display()
        else:
            A=Time(addTimehr,addTimemin)
            A.display()
    def display(self):
        print(self.hour,"Hours and " ,self.minutes,"Minutes")
    def displaymin(self):
        print(self.hour*60+self.minutes)

hour= int(input("enter hours"))
mintues= int(input("enter minutes"))
t=Time(hour,mintues)
t.display()
t.addTime()
t.displaymin()