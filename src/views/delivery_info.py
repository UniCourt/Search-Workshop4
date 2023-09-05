"""
To get delivery info
"""

from base import ApiBase
from utils.utils_schema import ORDER_STATS_INPUT_SCHEMA_VALIDATOR


class GetDeliveryInfo(ApiBase):
    """
    Class to get delivery info
    """
    def __init__(self, pg_con_obj):
        self.pg_con_obj = pg_con_obj

    def validator(self):
        """
        To validate input schema
        :return:
        """
        return ORDER_STATS_INPUT_SCHEMA_VALIDATOR

    def process_post(self, request_data):
        """
        Method to get delivery info from elasticsearch for given product_id
        :param request_data:
        :return:
        """
        try:
            order_id = request_data['order_id']
        except KeyError:
            return ('400', 'Bad Request', {})

        cursor = self.pg_con_obj.cursor()

        query = f'''SELECT id,customer_id, order_status, order_purchase_timestamp,
        order_approved_at, order_delivered_carrier_date, order_delivered_customer_date
        FROM "order" WHERE id=\'{order_id}\''''

        cursor.execute(query)

        row = cursor.fetchone()

        if not row:
            return ('404', 'Not Found', {})

        delivery_info_dict = {
            'order_id':                      row[0],
            'customer_id':                   row[1],
            'order_status':                  row[2],
            'order_purchase_timestamp':      row[3],
            'order_approved_at':             row[4],
            'order_delivered_carrier_date':  row[5],
            'order_delivered_customer_date': row[6]
        }

        query = f'''SELECT customer_zip_code_prefix, customer_city,
                customer_state FROM customer where id=\'{delivery_info_dict['customer_id']}\''''
        cursor.execute(query)

        row = cursor.fetchone()
        delivery_info_dict.update({
            'customer_zip_code_prefix': row[0],
            'customer_city':            row[1],
            'customer_state':           row[2]
        })

        return ('200', 'success', delivery_info_dict)
