from datetime import datetime
S1='12:25:00'
S2='13:00:00'

FMT= '%H:%M:%S'
time__=datetime.strptime(S2,FMT)-datetime.strptime(S1,FMT)
print(time__)
