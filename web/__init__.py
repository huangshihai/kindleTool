from web.json_encoder import NumpyCoder
import logging
from flask import Flask
from flask import request
import json
import kindletool
from web import config

# from .config import port
# from .custom_config import custom_path, get_custom_path
# custom_config

app = Flask(__name__)
log = logging.getLoggerClass()


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
    kindletool.pushBook(filename, bookid)
    return json.dumps({'rtnCode': 1, 'data': '成功'}, cls=NumpyCoder)


if __name__ == '__main__':
    app.run(port=config.port)
