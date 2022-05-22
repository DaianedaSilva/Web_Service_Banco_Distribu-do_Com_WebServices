import functools
import logging
from flask import request

tokenCliente1 = "6f986d8b-7cd7-4a2b-b645-5791f7b52ea8"
tokenCliente2 = "6a7de581-54d1-4e49-be22-128a00d958b8"
tokenCliente3 = "14457e72-720f-4afa-86a1-08c646aef0fb"
tokenCliente4 = "7ba5640b-3a25-4ecc-9a6e-9c9a129f2cb6"
tokenCliente5 = "29d0de06-6fad-4b8b-bbfe-bba2cc2c6297"
tokenCliente6 = "05281ee0-0bad-4eca-bab1-0fe76f8eb688"

tokens = [tokenCliente1, tokenCliente2, tokenCliente3,
          tokenCliente4, tokenCliente5, tokenCliente6]


def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        api_key = request.headers.get("x-api-key")
        if api_key == None:
            logging.warn("request bloked:: no api-key present")
            return {"message": "Please provide an API key"}, 400
        if tokens.count(api_key) >= 1:
            return func(*args, **kwargs)
        else:
            logging.warn("request bloked:: invalid api-key")
            return {"message": "The provided API key is not valid"}, 403
    return decorator
