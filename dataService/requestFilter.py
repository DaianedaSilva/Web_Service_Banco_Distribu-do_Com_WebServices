import functools
import logging
from flask import request
tokenServidor1 = "9cdcaba2-2e76-4a34-ae0a-3b3d54e0002d"
tokenServidor2 = "0a8168a8-6b9d-4d0b-9aef-99c5961b9f16"
tokenServidor3 = "854d6b6a-04d4-42d4-a440-8c45eca2f610"

tokens = [tokenServidor1, tokenServidor2, tokenServidor3]

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