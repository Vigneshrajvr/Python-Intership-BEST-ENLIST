from datetime import datetime, timedelta,date

date_time_str = '18/09/19 01:55:19'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)

d = datetime.today() - timedelta(days=5)
print(d)

print("Today's Date dt : ",date.today()) 

dt = datetime.combine(date.today(), datetime.min.time())

print("Type of dt : ",type(dt))

print("Date after converting to date time : ",dt)

print("Printing next seven days")

today = datetime.today()
for x in range(1, 8):
      val=today + timedelta(days=x)
      print(val.strftime("%A"))
