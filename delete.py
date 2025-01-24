import datetime
now = datetime.datetime.now()
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print (now.strftime("%H:%M:%S %Y-%m-%d ")+days[now.weekday()])