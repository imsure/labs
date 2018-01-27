from datetime import datetime
import pytz

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

now_utc = datetime.now(pytz.timezone('UTC'))
print('Current time in UTC:\n\t', now_utc.strftime(fmt))

# Convert to US/Central time
now_central = now_utc.astimezone(pytz.timezone('US/Central'))
print('Current time in US/Central:\n\t', now_central.strftime(fmt))
now_pacific = now_utc.astimezone(pytz.timezone('US/Pacific'))
print('Current time in US/Pacific:\n\t', now_pacific.strftime(fmt))

# Print all US time zones
for zone in pytz.all_timezones:
    if 'US' in zone:
        print(zone)
