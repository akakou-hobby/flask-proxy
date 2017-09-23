# coding:utf-8
'''ProxyをFlaskで書いてみました！

server.py
    このファイルはflask-proxyのサーバ側のコードです。
    flask-proxyの起動にはこのコードを実行してください。
'''
import socket
from flask import Flask, request


app = Flask(__name__)

class ServerForProxy:
    '''flask-proxyのサーバ側に関するクラス'''
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def server_routine(path):
        return 'response'



if __name__ == '__main__':
    app.run(debug=True)
