import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from web.json_encoder import NumpyCoder
import logging
from flask import Flask, request,make_response,send_from_directory
import json
import kindletool
from web import config
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
    # return '{"rtnCode": 1, "data": [{"__type": "js_ebook_data", "BID": "skRCEctOhICEBuNO%2bKTFbg%3d%3d", "Title": "\u6218\u56fd\u7b56\uff08\u5168\u4e8c\u518c\uff09\u7cbe--\u4e2d\u534e\u7ecf\u5178\u540d\u8457\u5168\u672c\u5168\u6ce8\u5168\u8bd1\u4e1b\u4e66[.azw3]", "Cover": "35/3515a694da357e9a78346f612390f882_s.jpg"}, {"__type": "js_ebook_data", "BID": "pMiqVzPE0EQRxsHJKMh9iA%3d%3d", "Title": "\u6218\u56fd\u7b56\uff1a\u8d85\u8d8a\u56fd\u754c\u4e0e\u9636\u7ea7\u7684\u8ba1\u8c0b\u5168\u4e66 (\u7ecf\u5178\u91cc\u7684\u4e2d\u56fd)[.mobi]", "Cover": "e3/e37fa07ce156b6bb2e8868cb1cf644b8_s.jpg"}, {"__type": "js_ebook_data", "BID": "OMtwW4%2bY1XOrmH%2fmBUwA2g%3d%3d", "Title": "\u6218\u56fd\u7b56[.mobi]", "Cover": "e7/e70e23ab3d6d520159d9705a79388513_s.jpg"}, {"__type": "js_ebook_data", "BID": "16%2fuHaZhBtOSuWFkBfcMmA%3d%3d", "Title": "\u5de6\u4f20\u6218\u56fd\u7b56\u8bb2\u6f14\u5f55 (\u5927\u5b66\u540d\u5e08\u8bb2\u8bfe\u5b9e\u5f55)[.azw3]", "Cover": "3f/3f25eff360eb6923a8400d411cee6bdf_s.jpg"}, {"__type": "js_ebook_data", "BID": "2UaHSWBxBMu5fbAQzOBVgw%3d%3d", "Title": "\u8c0b\u7565\u4e0e\u96c4\u8fa9\u5b9d\u5178--\u300a\u6218\u56fd\u7b56\u300b\u7cbe\u534e\u5168\u89e3\u6790[.mobi]", "Cover": "78/787b418fe93c08d5e16ee1dfce5d1d79_s.jpg"}, {"__type": "js_ebook_data", "BID": "C6ecq%2bV9CEbzQZhblcgWPA%3d%3d", "Title": "\u6218\u56fd\u7b56\uff08\u5168\u4e8c\u518c\uff09[.mobi]", "Cover": "13/1383a9e9a6abef57b951823b77dacecf_s.jpg"}, {"__type": "js_ebook_data", "BID": "mekNqXqhQF2XSRbxXTxlmw%3d%3d", "Title": "\u6218\u56fd\u7b56\uff1a\u6218\u56fd\u8c0b\u81e3\u7b56\u58eb\u6e38\u8bf4\u548c\u8fa9\u8bba\u8f91\u5f55\uff08\u56fd\u5b66\u7f51\u539f\u7248\u70b9\u6ce8\uff0c\u683e\u4fdd\u7fa4\u5ba1\u5b9a\uff09[.azw3]", "Cover": "a5/a568449572b88a92488fb421f2d2ae37_s.jpg"}, {"__type": "js_ebook_data", "BID": "Udm7eHJtegJr59tnrkGSJQ%3d%3d", "Title": "\u6218\u56fd\u7b56\uff08\u5168\u4e8c\u518c\uff09\u7cbe--\u4e2d\u534e\u7ecf\u5178\u540d\u8457\u5168\u672c\u5168\u6ce8\u5168\u8bd1\u4e1b\u4e66[.epub]", "Cover": "35/3515a694da357e9a78346f612390f882_s.jpg"}, {"__type": "js_ebook_data", "BID": "6VEhdMBqggbAlIhuiKYIiw%3d%3d", "Title": "\u6218\u56fd\u7b56[.epub]", "Cover": "28/28f6bdc78c1d03a4700035bb7173d798_s.jpg"}, {"__type": "js_ebook_data", "BID": "53ggGlpJ%2bSIz1DX0sLxITw%3d%3d", "Title": "\u8c0b\u7565\u4e0e\u96c4\u8fa9\u5b9d\u5178--\u300a\u6218\u56fd\u7b56\u300b\u7cbe\u534e\u5168\u89e3\u6790[.epub]", "Cover": "78/787b418fe93c08d5e16ee1dfce5d1d79_s.jpg"}, {"__type": "js_ebook_data", "BID": "MEZbX1CmtUx8ayinosYS%2fQ%3d%3d", "Title": "\u6218\u56fd\u7b56\u5168\u9274[.azw3]", "Cover": "60/60f059449143c25e2228357393705598_s.jpg"}, {"__type": "js_ebook_data", "BID": "YRHiGjt88f93g78a%2fef92w%3d%3d", "Title": "\u6218\u56fd\u7b56\u2014\u2014\u4e2d\u534e\u7ecf\u5178\u85cf\u4e66\uff08\u5347\u7ea7\u7248\uff09[.azw3]", "Cover": "16/16f41580cecc5ad8a1d38fffe8b8db21_s.jpg"}, {"__type": "js_ebook_data", "BID": "pMiqVzPE0ETKpjLZ%2f4rZQQ%3d%3d", "Title": "\u6218\u56fd\u7b56\uff1a\u8d85\u8d8a\u56fd\u754c\u4e0e\u9636\u7ea7\u7684\u8ba1\u8c0b\u5168\u4e66 (\u7ecf\u5178\u91cc\u7684\u4e2d\u56fd)[.azw3]", "Cover": "e3/e37fa07ce156b6bb2e8868cb1cf644b8_s.jpg"}, {"__type": "js_ebook_data", "BID": "eWXadS6b1677BNQFhmhc9A%3d%3d", "Title": "\u6218\u56fd\u7b56\uff08\u5168\u4e8c\u518c\uff09[.epub]", "Cover": "13/1383a9e9a6abef57b951823b77dacecf_s.jpg"}, {"__type": "js_ebook_data", "BID": "YRHiGjt88f%2fLliIYtmDvGw%3d%3d", "Title": "\u6218\u56fd\u7b56 (\u53e4\u5178\u540d\u8457\u767d\u6587\u672c)[.azw3]", "Cover": "fe/fe9b90eebc3ebf9e93695ab5194f5ca7_s.jpg"}, {"__type": "js_ebook_data", "BID": "1QfNELgr4D4hFvACK3aeDg%3d%3d", "Title": "\u6218\u56fd\u7b56\uff08\u5168\u4e8c\u518c\uff09\u7cbe--\u4e2d\u534e\u7ecf\u5178\u540d\u8457\u5168\u672c\u5168\u6ce8\u5168\u8bd1\u4e1b\u4e66[.mobi]", "Cover": "35/3515a694da357e9a78346f612390f882_s.jpg"}, {"__type": "js_ebook_data", "BID": "BYWYkVsX1YjA4ubFzbN5aw%3d%3d", "Title": "\u5de6\u4f20\u2022\u6218\u56fd\u7b56 (\u56fe\u8bf4\u5929\u4e0b\u56fd\u5b66\u4e66\u9662\u7cfb\u5217)[.azw3]", "Cover": "c9/c9d447524b26dcf7d3567f33abd14b96_s.jpg"}, {"__type": "js_ebook_data", "BID": "kKM2ABrO%2bbFz5eFL6AqXSw%3d%3d", "Title": "\u6218\u56fd\u7b56 (\u53e4\u5178\u540d\u8457\u767d\u6587\u672c)[.epub]", "Cover": "fe/fe9b90eebc3ebf9e93695ab5194f5ca7_s.jpg"}, {"__type": "js_ebook_data", "BID": "xAs6s3yho1C5WLbV8tB%2bog%3d%3d", "Title": "\u6218\u56fd\u7b56\u5168\u8bd1[.mobi]", "Cover": ""}, {"__type": "js_ebook_data", "BID": "%2bftjNgPB5xin1n%2fbwJAVnA%3d%3d", "Title": "\u4e2d\u4fe1\u56fd\u5b66\u5927\u5178\u00b7\u6218\u56fd\u7b56[.azw3]", "Cover": "dc/dc2274833d5544d5e344912255830e5e_s.jpg"}, {"__type": "js_ebook_data", "BID": "YRHiGjt88f9tCIVURORFqg%3d%3d", "Title": "\u6218\u56fd\u7b56 (\u6700\u7f8e\u56fd\u5b66)[.azw3]", "Cover": ""}, {"__type": "js_ebook_data", "BID": "JXDKiZAHY0diCrNF62bugA%3d%3d", "Title": "\u6218\u56fd\u7b56[.azw3]", "Cover": "f3/f38bf7c27dd777b3aad0a19064013f1c_s.jpg"}, {"__type": "js_ebook_data", "BID": "ELCc1NyezRzAalvZYC4ynA%3d%3d", "Title": "\u300a\u6218\u56fd\u7b56\u300b\u6c9f\u901a\u7b56[.azw3]", "Cover": "79/79d2488778839d13d2d63e719970bd4c_s.jpg"}, {"__type": "js_ebook_data", "BID": "bmjDyn8XeDkINVE7VMNAsA%3d%3d", "Title": "\u6218\u56fd\u7b56\uff08\u5168\u4e8c\u518c\uff09[.azw3]", "Cover": "4d/4d451961f140198a8094d6a83186cf41_s.jpg"}, {"__type": "js_ebook_data", "BID": "7yWcrlmJz9PltmzjVHAdKA%3d%3d", "Title": "\u6218\u56fd\u7b56\uff1a\u8d85\u8d8a\u56fd\u754c\u4e0e\u9636\u7ea7\u7684\u8ba1\u8c0b\u5168\u4e66 (\u7ecf\u5178\u91cc\u7684\u4e2d\u56fd)[.epub]", "Cover": "e3/e37fa07ce156b6bb2e8868cb1cf644b8_s.jpg"}, {"__type": "js_ebook_data", "BID": "41D2kam1uMyI9pTu%2bzylaA%3d%3d", "Title": "\u5de6\u4f20\u2022\u6218\u56fd\u7b56 (\u56fe\u8bf4\u5929\u4e0b\u56fd\u5b66\u4e66\u9662\u7cfb\u5217)[.mobi]", "Cover": "c9/c9d447524b26dcf7d3567f33abd14b96_s.jpg"}, {"__type": "js_ebook_data", "BID": "rho6NRFTGzBrI6u7AIz3DQ%3d%3d", "Title": "\u6218\u56fd\u7b56\u2014\u2014\u4e2d\u534e\u7ecf\u5178\u85cf\u4e66\uff08\u5347\u7ea7\u7248\uff09[.epub]", "Cover": "16/16f41580cecc5ad8a1d38fffe8b8db21_s.jpg"}, {"__type": "js_ebook_data", "BID": "hdIYG7EnFehjV31Pj%2f22oQ%3d%3d", "Title": "\u5de6\u4f20\u2022\u6218\u56fd\u7b56 (\u56fe\u8bf4\u5929\u4e0b\u56fd\u5b66\u4e66\u9662\u7cfb\u5217)[.epub]", "Cover": "17/174cfdfd4637143922db9741c433fbf6_s.jpg"}, {"__type": "js_ebook_data", "BID": "5aINuRWA4xT7m6DiibZryg%3d%3d", "Title": "\u6218\u56fd\u7b56\uff1a\u6218\u56fd\u8c0b\u81e3\u7b56\u58eb\u6e38\u8bf4\u548c\u8fa9\u8bba\u8f91\u5f55\uff08\u56fd\u5b66\u7f51\u539f\u7248\u70b9\u6ce8\uff0c\u683e\u4fdd\u7fa4\u5ba1\u5b9a\uff09[.epub]", "Cover": "a5/a568449572b88a92488fb421f2d2ae37_s.jpg"}, {"__type": "js_ebook_data", "BID": "yHp3QQW3PodYStmtI0r3ow%3d%3d", "Title": "\u6218\u56fd\u7b56\u5168\u9274\uff08\u73cd\u85cf\u7248\uff09[.azw3]", "Cover": "c7/c70c749eb25f50a30fed9c0dfb87a609_s.jpg"}, {"__type": "js_ebook_data", "BID": "MhKeo5LfVpwYoleGTa8iiQ%3d%3d", "Title": "\u6218\u56fd\u7b56\u5168\u9274[.epub]", "Cover": "60/60f059449143c25e2228357393705598_s.jpg"}, {"__type": "js_ebook_data", "BID": "1zijwsmjkRM%2f865WCNmWLg%3d%3d", "Title": "\u5de6\u4f20 \u5415\u6c0f\u6625\u79cb \u6218\u56fd\u7b56 (\u5bb6\u5ead\u4e66\u67b6)[.mobi]", "Cover": "63/63ccfe5a0426834c8cd77bcfa8646f22_s.jpg"}, {"__type": "js_ebook_data", "BID": "yHp3QQW3Pofyt8JQAhI3CQ%3d%3d", "Title": "\u6218\u56fd\u7b56\u5168\u9274\uff08\u73cd\u85cf\u7248\uff09[.epub]", "Cover": "c7/c70c749eb25f50a30fed9c0dfb87a609_s.jpg"}, {"__type": "js_ebook_data", "BID": "zlpALxzr8jgVeTsXBdvtSg%3d%3d", "Title": "\u6218\u56fd\u7b56\u5168\u9274\uff08\u73cd\u85cf\u7248\uff09[.mobi]", "Cover": "c7/c70c749eb25f50a30fed9c0dfb87a609_s.jpg"}, {"__type": "js_ebook_data", "BID": "1zijwsmjkROE3MWlKA8CUQ%3d%3d", "Title": "\u5de6\u4f20 \u5415\u6c0f\u6625\u79cb \u6218\u56fd\u7b56 (\u5bb6\u5ead\u4e66\u67b6)[.azw3]", "Cover": "63/63ccfe5a0426834c8cd77bcfa8646f22_s.jpg"}]}'


# 推送书籍
@app.route('/api/push_book', methods=['GET'])
def push_book():
    bookid = request.values.get('bookid')
    filename = request.values.get('filename')
    email = request.values.get('email')
    symbols = ['\\', '/', ':', '*', '?', '"', '|', '<', '>']
    for s in symbols:
        filename = filename.replace(s, '')
    kindletool.pushBook(filename, bookid, email)
    return json.dumps({'rtnCode': 1, 'data': '成功'}, cls=NumpyCoder)

# 下载书籍
@app.route('/api/download_book', methods=['GET'])
def download_book():
    bookid = request.values.get('bookid')
    filename = request.values.get('filename')
    symbols = ['\\', '/', ':', '*', '?', '"', '|', '<', '>']
    for s in symbols:
        filename = filename.replace(s, '')
    book_path = os.path.join(config.book_path, filename)
    if not os.path.exists(book_path):
        kindletool.downloadBook(filename, bookid)
    response = make_response(send_from_directory(config.book_path, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response

if __name__ == '__main__':
    app.run(port=config.port)
