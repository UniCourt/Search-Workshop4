"""
To get product stats info
"""
import json
from typing import Tuple

from base import ApiBase
from utils.utils_schema import PRODUCT_STATS_INPUT_SCHEMA_VALIDATOR


class GetProductStats(ApiBase):
    """
    Class to get product stats info
    """
    def __init__(self, es_con):
        super().__init__()
        self.es_con = es_con

    def validator(self):
        """
        To validate input schema
        :return:
        """
        return PRODUCT_STATS_INPUT_SCHEMA_VALIDATOR

    def process_post(self, request_data) -> Tuple[str, str, dict]:
        """
        Method to get product stats from elasticsearch for given product_id
        :param request_data:
        :return:
        """
        try:
            product_id = request_data['product_id']
        except KeyError:
            return ('400', 'Bad Request', {})

        q = {"query": {"match": {"productId": f"{product_id}"}}}
        resp = self.es_con.search(index="product_index", body=json.dumps(q))
        for hit in resp['hits']['hits']:
            return ('200', 'success', hit["_source"])

        return ('404', 'Not Found', {})