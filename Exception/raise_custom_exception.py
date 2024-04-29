class UserException(Exception):
    def __init__(self, msg):
        self.msg=msg
    def print_expection(self):
        print("User defined expection: ", self.msg)

try:
    raise UserException(" user raise exception")
except UserException as e:
    e.print_expection()
finally:
    print("clean up done")