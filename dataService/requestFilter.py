import functools
import logging
from flask import request
tokens = ["abadhasj4343nujdas", "asjdbasdsjkll345678*skad", "ansjdansjdas-89/*adsa"]

def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        api_key = request.headers.get("x-api-key")
        if api_key==None:
            logging.warn("request bloked:: no api-key present")
            return {"message": "Please provide an API key"}, 400
        if tokens.count(api_key)>=1:
            return func(*args, **kwargs)
        else:
            logging.warn("request bloked:: invalid api-key")
            return {"message": "The provided API key is not valid"}, 403
    return decorator