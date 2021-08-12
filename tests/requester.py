import json
import unittest

from src.requester.requester import *
from data.testdata.api_key import MY_API_KEY


class TestRequester(unittest.TestCase):

    # Standalone authentication failures

    def test_authenticate_wrong_datatype(self):
        r = Requester(3436)
        print(r.authenticated)
        print(r.session_token)

    def test_authenticate_wrong_apikey(self):
        r = Requester(MY_API_KEY)
        print(r.authenticated)
        print(r.session_token)

    def test_authenticate_no_apikey(self):
        r = Requester("")
        print(r.authenticated)
        print(r.session_token)

    # Standalone request -> param: "interface" failures

    def test_request_wrong_interface(self):
        r = Requester(MY_API_KEY)
        print(r.authenticated)
        print(r.session_token)
        params = {"orderNo": 1}
        r.request("articlo", "DELETE", params)
        print(r.response_status)
        print(r.return_value)

    # TODO Incorrect data type causes exception

    # def test_request_wrong_interface_datatype(self):
        # r = Requester(MY_API_KEY)
        # print(r.authenticated)
        # print(r.session_token)
        # params = {"orderNo": 1}
        # r.request(1, "DELETE", params)
        # print(r.response_status)
        # print(r.return_value)

    def test_request_no_interface(self):
        r = Requester(MY_API_KEY)
        print(r.authenticated)
        print(r.session_token)
        params = {"orderNo": 1}
        r.request("", "DELETE", params)
        print(r.response_status)
        print(r.return_value)

    # Token expired

    def test_request_expired_token(self):
        r = Requester(MY_API_KEY)
        print(r.session_token)
        # time.sleep(630)
        params = {"orderNo": 1}
        r.request("article", "DELETE", params)
        print(r.session_token)
        print(r.response_status)
        print(r.return_value)
        time.sleep(5)

    # Test for every interface of the cbooks api

    # I_ARTICLE

    def test_interface_article(self):
        r = Requester(MY_API_KEY)
        params = {"orderNo": "1"}
        r.request(I_ARTICLE, "DELETE", params)
        print(r.response_status)
        print(r.return_value)
        time.sleep(5)

    # I_ARTICLE_LIST

    def test_interface_article_list(self):
        r = Requester(MY_API_KEY)
        params = {"field": "orderNo", "showPrice": 1, "mediaType": 0}
        r.request(I_ARTICLE_LIST, "GET", params)
        print(r.response_status)
        print(r.return_value)
        time.sleep(5)

    # I_ARTICLE_STATUS

    def test_interface_article_status(self):
        r = Requester(MY_API_KEY)
        params = {"orderNo": 1}
        r.request(I_ARTICLE_STATUS, "GET", params)
        print(r.response_status)
        print(r.return_value)
        time.sleep(5)

    # I_FILE_STATUS

    def test_interface_file_status(self):
        r = Requester(MY_API_KEY)
        params = {"filename": "filename"}
        r.request(I_FILE_STATUS, "GET", params)
        print(r.response_status)
        print(r.return_value)
        time.sleep(5)

    # I_IMPORT_STATUS

    def test_interface_import_status(self):
        r = Requester(MY_API_KEY)
        r.request(I_IMPORT_STATUS, "GET")
        print(r.response_status)
        print(r.return_value)
        time.sleep(5)

    # I_ORDER

    def test_interface_order(self):
        r = Requester(MY_API_KEY)
        params = {"dateFrom": "2020-01-01", "dateTo": "2020-02-01"}
        r.request(I_ORDER, "GET", params)
        print(r.response_status)
        print(r.return_value)
        time.sleep(5)

    # I_ORDER_CANCEL

    # No test data available yet

    # def test_interface_order_cancel(self):
        # r = Requester(MY_API_KEY)
        # params = {"orderId": "..."}
        # r.request(I_ORDER_CANCEL, "PUT", params)
        # print(r.response_status)
        # print(r.return_value)
        # time.sleep(5)

    # I_ORDER_ITEM_CANCEL

    # No test data available yet

    # def test_interface_order_item_cancel(self):
        # r = Requester(MY_API_KEY)
        # params = {"orderItemId": "...", "mediaType": "..."}
        # r.request(I_ORDER_ITEM_CANCEL, "PUT", params)
        # print(r.response_status)
        # print(r.return_value)
        # time.sleep(5)

    # I_ORDER_STATUS

    # No test data available yet

    # def test_interface_order_item_cancel(self):
        # r = Requester(MY_API_KEY)
        # params = {"orderId": "...", "status": "..."}
        # r.request(I_ORDER_STATUS, "PUT", params)
        # print(r.response_status)
        # print(r.return_value)
        # time.sleep(5)


if __name__ == '__main__':
    unittest.main()
