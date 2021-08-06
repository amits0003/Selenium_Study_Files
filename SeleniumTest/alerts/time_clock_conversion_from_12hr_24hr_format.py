
s = '03:24:05PM'

splitted_string = s.split(":")

print(splitted_string[0])

hours = splitted_string[0]
hours_24_format = 0
minutes = splitted_string[1]
seconds = splitted_string[2]
if int(hours) < 12 and 'AM' in splitted_string[2]:
    hours_24_format = hours
elif int(hours) < 12 and 'PM' in splitted_string[2]:
    hours_24_format = int(hours)+12
elif int(hours) == 12 and 'AM' in splitted_string[2]:
    hours_24_format = '00'
elif int(hours) == 12 and 'PM' in splitted_string[2]:
    hours_24_format = 12
else:
    print('invalid time')

if 'AM' in splitted_string[2]:
    seconds = seconds.rstrip('AM')
elif 'PM' in splitted_string[2]:
    seconds = seconds.rstrip('PM')

print(str(hours_24_format)+':'+splitted_string[1]+':'+str(seconds))