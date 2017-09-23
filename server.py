# coding:utf-8
'''ProxyをFlaskで書いてみました！

server.py
    このファイルはflask-proxyのサーバ側のコードです。
    flask-proxyの起動にはこのコードを実行してください。
'''
import socket
from flask import Flask, request


app = Flask(__name__)

class FlaskProxy:
    '''flask-proxyのサーバ側に関するクラス'''
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def server_routine(self, path):
        '''クライアントからレスポンスを送られてから、レスポンスの返答まで'''
        response_dict = generate_client_data(requests)
        return 'response'

    def generate_client_data(self, requests):
        '''HTTPリクエストの生成'''
        # HTTPリクエスト（文字列）の生成
        header = request.method + ' ' + \
            request.full_path + '\n' + \
            str(request.headers)

        # URLの生成
        host = request.url_root.split('/')
        host = host[2]

        # Request辞書（後に使用）を作成
        return request_dict = {
            'host': client_url,
            'port': 80,
            'header': client_request,
            'encode': 'utf-8'
        }


if __name__ == '__main__':
    flask_proxy = FlaskProxy()
    app.run(debug=True)
