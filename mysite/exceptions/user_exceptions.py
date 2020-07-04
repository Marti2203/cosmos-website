class UserException(Exception):
    pass


class UserNotAdminException(UserException):
    pass


class UserNotLoggedInException(UserException):
    pass
