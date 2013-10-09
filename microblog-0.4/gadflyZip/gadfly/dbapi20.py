
# -*- coding: UTF-8 -*-
"""implements the db api 2.0 for the gadfly database
"""

# $Id: dbapi20.py,v 1.2 2003/10/09 03:15:01 zenzen Exp $

from database import gadfly, error
from dbapi20error import *

import os
import os.path

__all__ = ['connect', 'apilevel', 'threadsafety', 'paramstyle']

apilevel = '2.0'

# see email from the gadfly list
threadsafety = 1 

paramstyle = 'qmark'

def connect(*args, **kwargs):
    connection = None
    try:
        connection = Connection(*args, **kwargs)
    except IOError, ioe:
        raise DatabaseError(str(ioe))
    return connection

class Connection:

    # DB API 2.0 Optional Extension
    Warning = Warning
    Error = Error
    InterfaceError = InterfaceError
    DatabaseError = DatabaseError
    OperationalError = OperationalError
    IntegrityError = IntegrityError
    InternalError = InternalError
    ProgrammingError = ProgrammingError
    NotSupportedError = NotSupportedError
    
    def __init__(self, *args, **kwargs):
        self.closed = 0
        self._gadfly = gadfly(*args, **kwargs)
        
    def __checkClosed(self):
        if self.closed:
            raise OperationalError('Connection already closed.')
        
    def close(self):
        self.__checkClosed()
        self.closed = 1
        self._gadfly.close()
        
    def commit(self):
        self.__checkClosed()
        self._gadfly.commit()
        
    def rollback(self):
        self.__checkClosed()
        self._gadfly.rollback()
        
        
    def cursor(self):
        """
        """
        self.__checkClosed()
        cursor = self._gadfly.cursor()
        return Cursor(self, cursor)

class Cursor:
    
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
        self.closed = 0

        # api - attribute
        self.description = None
        self.rowcount = -1
        self.arraysize = 1

    def __checkClosed(self):
        if self.closed or self.connection.closed:
            raise OperationalError('Cursor already closed.')
     
    def __makeRowCount(self):
        self.rowcount = -1
        
    def callproc(self, procname, *parameters):
        self.__checkClosed()
        return self.cursor(procname, *parameters)
    
    def close(self):
        self.__checkClosed()
        self.closed = 1
        return self.cursor.close()
    
    def execute(self, operation, *parameters):
        self.__checkClosed()
        self.cursor.execute(operation, *parameters)
        self.description = self.cursor.description
        self.__makeRowCount()
        
    def executemany(self, operation, seq_of_parameters):
        self.__checkClosed()
        for parameters in seq_of_parameters:
            self.execute(operation, parameters)
    
    def fetchone(self):
        result = None
        self.__checkClosed()

        try:
            result = self.cursor.fetchone()
        except error, message:
            # gadfly use string exception and the only way to
            # difference between reason is the message
            if message == "no more results":
                pass
            else:
                raise OperationalError(message)
        except AttributeError, e:
            raise OperationalError(str(e))
        return result
    
    def fetchmany(self, size=None):
        result = None
        self.__checkClosed()

        if size is None:
            size = self.arraysize

        try:
            result = self.cursor.fetchmany(size)
        except error, message:
            raise OperationalError(message)
        except AttributeError, e:
            raise OperationalError(str(e))
        
        return result
    
    def fetchall(self):
        result = None
        self.__checkClosed()
        try:
            result = self.cursor.fetchall()
        except error, message:
            raise OperationalError(message)
        except AttributeError, e:
            raise OperationalError(str(e))
        return result
    
    def setinputsizes(self, sizes):
        return self.cursor.setinputsizes(sizes)
    
    def setoutputsize(self, size, column=None):
        return self.cursor.setoutputsize(size, column)
    
