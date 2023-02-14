#task1
"""from datetime import datetime,timedelta
today=datetime.now()
def subt(date, days):
    return date-timedelta(days=days)
print(f'The date is: {subt(today, 5)}')
    """
#task2
"""import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday was:", yesterday.strftime('%d/%m/%Y'))
print("Today is:", today.strftime('%d/%m/%Y'))
print("Tomorrow is:", tomorrow.strftime('%d/%m/%Y'))
"""
#task3
"""import datetime
dt_with_microseconds = datetime.datetime.now()
dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)
print("Datetime without microseconds:", dt_without_microseconds)
"""
#task4
"""
import datetime
date1 = datetime.datetime(2022, 2, 14, 12, 0, 0)
date2 = datetime.datetime(2022, 2, 14, 13, 30, 0)
diff_seconds = (date2 - date1).total_seconds()
print("Difference in seconds:", diff_seconds)
"""