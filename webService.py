#import dataService

from flask import Flask
app = Flask(__name__)
app.run(debug=True)

tokens = ["abadhasj4343nujdas", "asjdbasdsjkll345678*skad", "ansjdansjdas-89/*adsa"]

@app.route('/deposito/<acnt>/<amt>',methods=['GET'])
def deposito(acnt, amt):
    str = 'deposito de ' + acnt + ' para' + amt
    return str

@app.route('/saque/<acnt>/<amt>',methods=['GET'])
def saque(acnt, amt):
    str = 'saque de ' + acnt + ' para' + amt
    return str

@app.route('/saldo/<acnt>',methods=['GET'])
def saldo(acnt):
    str = 'Saldo de ' + acnt
    return str

@app.route('/transferencia/<acnt_orig>/<acnt_dest>/<amt>',methods=['GET'])
def transferencia(acnt_orig, acnt_dest,  amt):
    str = 'transferencia de ' + acnt_orig + " para " + acnt_dest + " no valor de " + amt
    return str
