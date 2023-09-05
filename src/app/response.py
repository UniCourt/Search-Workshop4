"""
Response object
"""
#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify


class ApiResponse(object):
    """
    Class to create response object
    """
    SUCCESS_STATUS_CODE: int = 200
    NO_CONTENT_STATUS_CODE: int = 204

    @classmethod
    def get(cls, status: str, message: str, result: (dict, None) = None, status_code: int = 200):
        """
        Create final response object
        """
        data = {'status': status, 'message': message}
        if result is not None:
            data['data'] = result

        content = jsonify(data)
        response = Flask(__name__).make_response((content, status_code))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response


