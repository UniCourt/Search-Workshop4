"""
Creating Flask APIs
"""
__author__ = "UniCourt Inc"
__version__ = "v1.0.0"
__maintainer__ = "Search - Core & API"
__email__ = "eng-search@unicourt.com"

from flask import Flask, request
import os
import sys
import logging
import logstash

sys.path.insert(0, '/src')

from views.delivery_info import GetDeliveryInfo
from views.product_stats import GetProductStats
from utils.utils_es import get_es_connection
from utils.utils_postgres import set_connection
from utils.utils_constants import LogDict

LOGGER = logging.getLogger("search_logger")
PG_CON = set_connection(LOGGER)

app = Flask(__name__)
ES_CON = get_es_connection(os.environ['ES_HOST'], os.environ['ES_PORT'])
app.logger.setLevel(logging.INFO)
app.logger.addHandler(logstash.TCPLogstashHandler("127.0.0.1", 5959, version=1))


@app.route('/DeliveryInfo', methods=['POST'])
def get_delivery_info():
    """
    Method to return delivery info for the given product_id
    :return:
    """
    log_dict = LogDict.REQUEST_INFO_DICT
    post_data = request.get_json()
    log_dict["Request_data"] = post_data
    try:
        delivery_info_obj = GetDeliveryInfo(PG_CON)
        result = delivery_info_obj.process(post_data)
    except Exception as exception:
        log_dict["Status"] = "500"
        log_dict["Message"] = "FAILURE"
        app.logger.setLevel(logging.ERROR)
        app.logger.error(log_dict)
        return ('500', 'Internal server error', {})

    log_dict["Status"] = result.status
    app.logger.info(log_dict)
    return result


@app.route('/ProductStats', methods=['POST'])
def get_product_stats():
    """
    Method to return products stats info for the given product_id
    :return:
    """
    log_dict = LogDict.REQUEST_INFO_DICT
    post_data = request.get_json()
    log_dict["Request_data"] = post_data
    try:
        product_stats_obj = GetProductStats(ES_CON)
        result = product_stats_obj.process(post_data)
    except Exception as exception:
        log_dict["Status"] = "500"
        log_dict["Message"] = "FAILURE"
        app.logger.setLevel(logging.ERROR)
        app.logger.error(log_dict)
        return ('500', 'Internal server error', {})

    log_dict["Status"] = result.status
    log_dict["Message"] = "SUCCESS"
    app.logger.info(log_dict)

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')
