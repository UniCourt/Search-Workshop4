"""
Validation types and status
"""


class ValidationTypes(object):
    """
    List of validation types
    """
    URL_ERROR = 'URL_NOT_FOUND'
    INVALID_JSON_SCHEMA = 'INVALID_JSON_SCHEMA'
    UNPROCESSABLE_ENTITY = 'UNPROCESSABLE_ENTITY'
    INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR'


class Status(object):
    """
    List of status types
    """
    SUCCESS = 'success'
    FAILURE = 'failure'


class LogDict(object):
    """
    Log dict
    """
    REQUEST_INFO_DICT = {
        "Status": "",
        "Request_data": ""
    }
