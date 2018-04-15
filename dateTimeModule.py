'''
 Datetime Module tutorial
 Followed: https://www.youtube.com/watch?v=eirjjyP2qcQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=24
'''

import datetime
import pytz
# two different types, naive (simple) and aware (considers timezones, etc)

# create a datetime object (don't add 0's before dates, will cause error)
d = datetime.date(2016, 7, 24)
print("A random day: ", d)

tday = datetime.date.today()
print("Today's date: ", tday)
print("Current Year: ", tday.year)
print("Current Month: ", tday.month)
print("Current Day: ", tday.day)
print("Day of the week: ", tday.weekday())
print("Day of the week: ", tday.isoweekday())

# time delta
tdelta = datetime.timedelta(days=7)
print("\nDate a week from now: ", tday + tdelta)

bday = datetime.date(2018, 4, 17)
# create time delta calculation
till_bday = bday - tday
print("\nDays until birthday: ", till_bday.days)
print("Total amount of seconds before birthday: ", till_bday.total_seconds())


############### TIME ##############
t = datetime.time(9, 30, 45, 100000) 	# hours, minutes seconds, ms
print("\nTime: ", t)
print("Hour: ", t.hour)

############## DATETIME ###########
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000) 
print("\nDate & Time: ", dt)
print("Just Date: ", dt.date())
print("Just Time: ", dt.time())
print("Just Year: ", dt.year)

# create a delta and add to delta
tdelta = datetime.timedelta(days=7)
print("A week later: ", dt + tdelta)

tdelta = datetime.timedelta(hours=12)
print("12 hours later: ", dt + tdelta)

############### TODAY/NOW ###########
dt_today = datetime.datetime.today()		# current local time with no timezone
dt_now = datetime.datetime.now()			# gives an option to insert a timezone
dt_utcnow = datetime.datetime.utcnow()		# 

print("\ntoday(): ", dt_today)
print("now(): ", dt_now)
print("utcnow(): ", dt_utcnow)

############# TIMEZONES ############
dt = datetime.datetime(2018, 4, 10, 8, 18, 45, tzinfo=pytz.UTC)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print("\nnow() w/timezone: ", dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print("utcnow() w/replace(tzinfo): ", dt_utcnow)


dt_utcnow - datetime.datetime.now(tz=pytz.UTC)
print("normal: ", dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print("mountain: ", dt_mtn)

# print out all timezones
print("ALL TIMEZONES:")
for tz in pytz.all_timezones:
	print(tz)

# have a naive datetime and make it timezone aware
dt_mtn2 = datetime.datetime.now()
print("\nNaive: ", dt_mtn2)    # prints out: 2018-04-15 16:28:02.426157-06:00 <- not timezone aware

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn2 = mtn_tz.localize(dt_mtn2)
dt_east = dt_mtn2.astimezone(pytz.timezone('US/Eastern'))

print("Timezone aware to Eastern: ", dt_east)


dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print("\nFormat time: ", dt_mtn.strftime('%B %d, %Y'))

dt_str = 'April 15, 2018'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print("Format above string: ", dt)

# strftime - Datetime to String
# strptime - String to Datetime
