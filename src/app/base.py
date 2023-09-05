"""
API base
"""
#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import inspect
import logging
from abc import abstractmethod
from typing import Tuple

from fastjsonschema.exceptions import JsonSchemaException
from flask import request
from flask.views import MethodView

from response import ApiResponse
from utils.utils_constants import Status, ValidationTypes


logger = logging.getLogger("search_logger")
__author__ = "UniCourt India"
__version__ = "v3.2020.02.25"
__maintainer__ = "Researcher"


class ApiBase(MethodView):
    """
    Base class for APIs
    """
    def __init__(self):
        super().__init__()
        self.__validator = None
        self._post_data = None


    @property
    @abstractmethod
    def validator(self):
        """
        Abstract method
        :return:
        """
        return self.__validator

    def validate_schema(self, request_data):
        """
        Method to validate the request_data by calling the validator
        :param request_data:
        :return:
        """
        try:
            self.validator()
            return Status.SUCCESS, None, None
        except JsonSchemaException as error:
            error_message = 'The request was well-formed but was unable to be followed due to semantic errors.'
            validation_type = ValidationTypes.UNPROCESSABLE_ENTITY
            return Status.FAILURE, validation_type, error_message

    @abstractmethod
    def process_post(self, request_data) -> Tuple[str, str, dict]:
        """
        Abstract method
        :param request_data:
        :return:
        """
        return Status.FAILURE, "", {}

    def process(self, request_data):
        """
        To process the request data by calling process_post
        :param request_data:
        :return:
        """
        self._post_data = request_data
        self.validate_schema(request_data=request_data)
        (status, message, data) = self.process_post(request_data=request_data)

        response_message = ApiResponse.get(status, message, result=data)
        return response_message


