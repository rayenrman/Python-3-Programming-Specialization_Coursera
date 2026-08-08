str_secs = input('Please enter the number of seconds you wish to convert: ')
total_secs = int(str_secs)
hours = total_secs // 3600
secs_remaining = total_secs % 3600
mins = secs_remaining // 60
secs = secs_remaining % 60
print('hours =', hours, ', minutes =', mins, ', seconds =', secs)