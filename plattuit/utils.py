'''General utilities for the application. Local applications can also have
utilities per module or app.
'''

# timezone
from django.utils import timezone


def time_zone():
    '''Returns correct time in the current timezone'''
    return timezone.localtime(timezone.now())
