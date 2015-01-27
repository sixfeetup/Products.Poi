## Script (Python) "checkForDate"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=value, format
##title=Get the date, or return an empty string
##

from DateTime import DateTime

if value:
    try:
        d = DateTime(value)
    except:
        return value

    return d.strftime(format)
    
else:
    return value