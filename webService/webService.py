import logging
from flask import Flask

from requestFilter import api_required

logging.basicConfig(filename='logs.log', level=logging.DEBUG)

app = Flask(__name__)
app.run(debug=True)

@api_required
@app.route('/deposito/<acnt>/<amt>',methods=['POST'])
def deposito(acnt, amt):
    str = 'deposito de ' + acnt + ' para' + amt
    logging.info(str)
    return str

@api_required
@app.route('/saque/<acnt>/<amt>',methods=['POST'])
def saque(acnt, amt):
    str = 'saque de ' + acnt + ' para' + amt
    logging.info(str)
    return str

@api_required
@app.route('/saldo/<acnt>',methods=['GET'])
@api_required
def saldo(acnt):
    str = 'Saldo de ' + acnt
    logging.info(str)
    return str

@app.route('/transferencia/<acnt_orig>/<acnt_dest>/<amt>',methods=['POST'])
def transferencia(acnt_orig, acnt_dest,  amt):
    str = 'transferencia de ' + acnt_orig + " para " + acnt_dest + " no valor de " + amt
    logging.info(str)
    return str
