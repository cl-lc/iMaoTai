import time
import datetime

# int(time.mktime(datetime.date.today().timetuple())) * 1000


print(time.time())
print(time.mktime(datetime.date.today().timetuple()))
print(int(time.mktime(datetime.date.today().timetuple())) * 1000)