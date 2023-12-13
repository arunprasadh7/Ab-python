# User defined exceptions - as users we can create our own exceptions

# creating our own error class called MyError

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        # return self.msg
        return 'Creating my own exception for handling errors'


try:
    raise MyError('Some Error occurred')

except MyError as e:
    print(e)