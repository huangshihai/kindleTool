import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from web.json_encoder import NumpyCoder
import logging
from flask import Flask, request
import json
import kindletool
from web import config

app = Flask(__name__)
log = logging.getLoggerClass()


# 首页
@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


# 搜索
@app.route('/api/search', methods=['GET'])
def search():
    bookname = request.values.get('bookname')
    booklist = []
    if bookname:
        print(bookname)
        booklist = kindletool.searchBook(bookname)
    print(booklist)
    return json.dumps({'rtnCode': 1, 'data': booklist}, cls=NumpyCoder)


# 推送书籍
@app.route('/api/push_book', methods=['GET'])
def push_book():
    bookid = request.values.get('bookid')
    filename = request.values.get('filename')
    email = request.values.get('email')
    kindletool.pushBook(filename, bookid, email)
    return json.dumps({'rtnCode': 1, 'data': '成功'}, cls=NumpyCoder)


if __name__ == '__main__':
    app.run(port=config.port)
