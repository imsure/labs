from datetime import datetime

fmt_whole = "%Y-%m-%d %H:%M:%S"
fmt_date = "%Y-%m-%d"
fmt_time = "%H:%M:%S"

now_dt = datetime.now()
print(now_dt.strftime(fmt_whole))
print(now_dt.strftime(fmt_date))
print(now_dt.strftime(fmt_time))
