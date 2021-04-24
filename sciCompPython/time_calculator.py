def add_time(start, duration, day=None):
    time, ampm = start.split()
    hour, minute = time.split(':')
    hour1, minute1 = duration.split(':')
    hour, hour1, minute, minute1 = int(hour), int(hour1), int(minute), int(minute1)

    if ampm == 'PM': hour += 12

    new_hour = hour + hour1
    new_minute = minute + minute1
    if new_minute > 60: new_hour += 1; new_minute -= 60

    days = new_hour // 24
    new_hour %= 24
    if new_hour < 12: ampm = 'AM'
    else: new_hour -= 12; ampm = 'PM'
    if new_hour == 0: new_hour = 12
    new_time = f'{new_hour}:{str(new_minute).zfill(2)} {ampm}'

    if day:
        d_arr = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        new_time += f', {d_arr[(d_arr.index(day.lower().capitalize()) + days) % 7]}'
    if days: new_time += f' ({days} days later)' if days > 1 else f' (next day)'

    return new_time
