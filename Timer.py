from win10toast import ToastNotifier
import time
import datetime as dt
t = ToastNotifier()

m4_5 = 270
m5 = 300
m10 = 600
m15 = 900
m30 = 1800
hr1 = 3600
hr2 = 7200

print('\n\n\n\n\n')

t.show_toast("Startup warning", "You have 5 mins until your 1 hr study period starts")
print('5 min warning', dt.datetime.now())
time.sleep(m5)

t.show_toast('Timer Started', 'Your 1hr timer has started')
print('time started', dt.datetime.now())
time.sleep(m30)

t.show_toast('Time Reminder', 'You have 30 mins left')
print('30 mins left', dt.datetime.now())
time.sleep(m30)

t.show_toast('Have a break', 'Your 1hr period is now over so go take a 15 min break')
print('start break', dt.datetime.now())
time.sleep(m10)

t.show_toast('5 Min reminder', 'Your break ends in 5 mins')
print('5 min reminder', dt.datetime.now())
time.sleep(m4_5)

t.show_toast('Startup warning', 'You have 30 seconds until your 1hr starts')
print('30 seconds until start', dt.datetime.now())
time.sleep(30)

t.show_toast('Timer started', 'Your 1hr timer has started')
print('Timer started', dt.datetime.now())
time.sleep(30)

t.show_toast('Time Reminder', 'You have 30 mins left')
print('30 mins left', dt.datetime.now())
time.sleep(m30)

t.show_toast('Have a break', 'Your 1hr period is now over so go take a 15 min break')
print('Have a break', dt.datetime.now())
time.sleep(30)

t.show_toast("WARNING", 'This code has now ended')
print('code has ended', dt.datetime.now())
