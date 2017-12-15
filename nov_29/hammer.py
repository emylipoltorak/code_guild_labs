def meal_times():
    input_time = input('What time is it?: ').upper().lstrip('0')
    time = input_time.replace(':','.')
    if float(time.rstrip('APM')) > 12.59:
        raise ValueError('Please enter a valid time, using the 12hr clock and AM or PM.')
    if time.startswith('12'):
        if time.endswith('AM'):
            time = float(time.rstrip('AM'))+12
        elif time.endswith('PM'):
            time = float(time.rstrip('PM'))
        else:
            raise ValueError('Please enter a valid time, using the 12hr clock and AM or PM.')
    elif time.endswith('AM'):
        time = float(time.rstrip('AM'))
    elif time.endswith('PM'):
        time = float(time.rstrip('PM'))+12
    else:
        raise ValueError('Please enter a valid time, using the 12hr clock and AM or PM.')
    if time >= 7.0 and time <= 9.0:
        return 'It\'s {}. Time for breakfast!'.format(input_time)
    elif time >= 12.0 and time <= 14.0:
        return 'It\'s {}. Time for lunch!'.format(input_time)
    elif time >= 19.0 and time <= 21.0:
        return 'It\'s {}. Time for dinner!'.format(input_time)
    elif (time >= 22.0 and time <=24.59) or (time <= 4.0):
        return 'Stop. Hammer Time.'
    else:
        return 'You\'re traveling through an unknown period. Neither eating nor hammering is permitted at this time.'

print(meal_times())
