"""
Schema validation for the request data
"""
from fastjsonschema import compile

__author__ = "UniCourt Inc"
__version__ = "v1.0.0"
__maintainer__ = "Search - Core & API"
__email__ = "eng-search@unicourt.com"

PRODUCT_STATS_INPUT_SCHEMA = {
    "title": "Product Stats Schema",
    "type": "object",
    "properties": {
        "product_id": {
            "type": "string"
        }
    },
    "required": ["product_id"]
}
PRODUCT_STATS_INPUT_SCHEMA_VALIDATOR = compile(PRODUCT_STATS_INPUT_SCHEMA)

ORDER_STATS_INPUT_SCHEMA = {
    "title": "Order Stats Schema",
    "type": "object",
    "properties": {
        "order_id": {
            "type": "string"
        }
    },
    "required": ["order_id"]
}

ORDER_STATS_INPUT_SCHEMA_VALIDATOR = compile(ORDER_STATS_INPUT_SCHEMA)