# https://www.booklooker.de/pages/rest_api.php

API_BASE_URL = "https://api.booklooker.de/2.0/"

# HTTP methods
GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"
OPTIONS = "OPTIONS"

# Interfaces
I_AUTHENTICATE = "authenticate"
I_ARTICLE = "article"
I_ARTICLE_LIST = "article_list"
I_ARTICLE_STATUS = "article_status"
I_FILE_IMPORT = "file_import"
I_FILE_STATUS = "file_status"
I_IMPORT_STATUS = "import_status"
I_ORDER = "order"
I_ORDER_CANCEL = "order_cancel"
I_ORDER_ITEM_CANCEL = "order_item_cancel"
I_ORDER_STATUS = "order_status"

# Value keys
TOKEN_KEY = "?token="
RESPONSE_STATUS = "status"
RETURN_VALUE = "returnValue"
API_KEY = "apiKey"

# Response status
OK = "OK"
NOT_OK = "NOK"

# General used return values (except interface authenticate)
QUOTA_EXCEEDED = "QUOTA_EXCEEDED"
TOKEN_EXPIRED = "TOKEN_EXPIRED"

# Of the session token in minutes
EXPIRY_TIME = 10

