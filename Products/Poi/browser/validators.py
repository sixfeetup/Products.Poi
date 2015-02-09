from datetime import datetime
from Products.validation import validation
from Products.validation.interfaces.IValidator import IValidator
from zope.interface import implements

class DateValidator:
    """Check that we have a valid date entered as MM/DD/YYYY
    """
    implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        try:
            datetime.strptime(value, '%m/%d/%Y')
        except:
            return 'Enter a required due date using the MM/DD/YYYY format.'


DateValidator = DateValidator('DateValidator',)
validation.register(DateValidator)
