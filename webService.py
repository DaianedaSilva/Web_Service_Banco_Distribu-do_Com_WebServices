#import dataService
import functools
import logging
from turtle import st
from flask import Flask, request

logging.basicConfig(filename='logs.log', level=logging.DEBUG)

app = Flask(__name__)
app.run(debug=True)

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

@app.route('/deposito/<acnt>/<amt>',methods=['GET'])
def deposito(acnt, amt):
    str = 'deposito de ' + acnt + ' para' + amt
    logging.info(str)
    return str

@app.route('/saque/<acnt>/<amt>',methods=['GET'])
def saque(acnt, amt):
    str = 'saque de ' + acnt + ' para' + amt
    logging.info(str)
    return str

@app.route('/saldo/<acnt>',methods=['GET'])
@api_required
def saldo(acnt):
    str = 'Saldo de ' + acnt
    logging.info(str)
    return str

@app.route('/transferencia/<acnt_orig>/<acnt_dest>/<amt>',methods=['GET'])
def transferencia(acnt_orig, acnt_dest,  amt):
    str = 'transferencia de ' + acnt_orig + " para " + acnt_dest + " no valor de " + amt
    logging.info(str)
    return str
