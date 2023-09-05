"""
Elastic search connection
"""
import json

from elasticsearch import Elasticsearch

__author__ = "UniCourt Inc"
__version__ = "v1.0.0"
__maintainer__ = "Search - Core & API"
__email__ = "eng-search@unicourt.com"


def get_es_connection(host: str, port: str):
    """
    Creates elasticsearch connection
    :param host:
    :param port:
    :return:
    """
    try:
        elastic = Elasticsearch(f"http://{host}:{port}")
        print("Connected to ES !!")
        return elastic
    except Exception as error:
        print("Elasticsearch Client Error:", error)
        raise error
