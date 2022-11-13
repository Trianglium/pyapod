from requests.exceptions import RequestException

class PyApodException(Exception):
    # Base Exception for all exceptions
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class PyApodRequestsException(RequestException):
    # Exceptions caused using requests library
    pass


class PyApodDateException(PyApodException):
    # Exception raised when `date` is wrong
    pass

class PyApodStartDateException(PyApodException):
    # Exception raised when `start_date` is wrong
    pass

class PyApodEndDateException(PyApodException):
    # Exception raised when `end_date` is wrong
    pass

class PyApodApiKeyException(PyApodException):
    # Exception raised when `api_key` is wrong
    pass

class PyApodCountException(PyApodException):
    # Exception raised when `count` is wrong
    pass

class PyApodThumbsException(PyApodException):
    # Exception raised when `thumbs` is wrong
    pass

class PyApodInvalidAPIResponseException(PyApodException):
    # Exception raised when apod API response is not parse-able
    pass