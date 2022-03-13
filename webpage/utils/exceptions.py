class MyFlightException(BaseException):
    ...


class APIRequestError(MyFlightException):
    ...


class NotFound(MyFlightException):
    ...
