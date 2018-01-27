from timezonefinder import TimezoneFinder

tf = TimezoneFinder()
lat = 32.23114
lon = -110.94548
print(tf.timezone_at(lng=lon, lat=lat))
