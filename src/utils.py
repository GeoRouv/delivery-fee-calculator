from datetime import datetime

def is_time_between(begin_time, end_time, check_time=None):
    '''
    Checks if given time() is between a range of two other times()
    '''
    
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()

    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time
