# coding:utf-8
'''ProxyをFlaskで書いてみました！

server.py
    このファイルはflask-proxyのサーバ側のコードです。
    flask-proxyの起動にはこのコードを実行してください。
'''
import socket
from flask import Flask, request

import tcpclient.low_layer_http_client


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def server_routine(path):
    '''クライアントからレスポンスを送られてから、レスポンスの返答まで'''
    request_dict = generate_client_data(request)
    response = client_routine(request_dict)
    return response['body']

def generate_client_data(request):
    '''HTTPリクエストの生成'''
    # HTTPリクエスト（文字列）の生成
    header = request.method + ' ' + \
        request.full_path + '\n' + \
        str(request.headers)

    # URLの生成
    host = request.url_root.split('/')
    host = host[2]

    # Request辞書（後に使用）を作成
    return {
        'host': host,
        'port': 80,
        'header': header,
        'encode': 'utf-8'
    }

def client_routine(request):
    '''HTTPリクエストの送信＆HTTPレスポンスの受取'''
    client = tcpclient.low_layer_http_client.TCP(host='', port='', request=request)
    client.connect()
    client.send(request['header'])
    response = client.get_response()
    client.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)
