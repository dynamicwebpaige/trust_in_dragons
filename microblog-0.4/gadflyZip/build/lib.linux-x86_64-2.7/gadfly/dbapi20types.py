
# -*- coding: UTF-8 -*-
"""defines the types for db api 2.0
"""
# $Id: dbapi20types.py,v 1.3 2003/10/09 11:43:04 zenzen Exp $

from time import gmtime

# only a mapping to the python standard types
STRING = str
BINARY = str
NUMBER = float
DATETIME = str
ROWID = str

def Date(year, month, day):
    """This function constructs an object holding a date value.
    """
    return "%04d-%02d-%02d" % (year, month, day)

def Time(hour, minute, second):
    """This function constructs an object holding a time value.
    """
    return "%02d:%02d:%02d" % (hour, minute, second)
    
def Timestamp(year, month, day, hour, minute, second):
    """This function constructs an object holding a time stamp
    value.
    """
    return "%04d-%02d-%02d %02d:%02d:%02d" % (
            year, month, day, hour, minute, second
            )
    
def DateFromTicks(ticks):
    """This function constructs an object holding a date value
    from the given ticks value (number of seconds since the
    epoch; see the documentation of the standard Python time
    module for details).
    """
    date = gmtime(ticks)
    return "%04d-%02d-%02d" % date[:3]
    
def TimeFromTicks(ticks):
    """This function constructs an object holding a time value
    from the given ticks value (number of seconds since the
    epoch; see the documentation of the standard Python time
    module for details).
    """
    time = gmtime(ticks)
    return "%02d:%02d:%02d" % time[3:6]
    
def TimestampFromTicks(ticks):
    """This function constructs an object holding a time stamp
    value from the given ticks value (number of seconds since
    the epoch; see the documentation of the standard Python
    time module for details).
    """
    time = gmtime(ticks)
    return "%04d-%02d-%02d %02d:%02d:%02d" % time[:6]
    
def Binary(string):
    """This function constructs an object capable of holding a
    binary (long) string value.
    """
    return str(string)

