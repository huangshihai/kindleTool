# -*- coding: utf-8 -*-
import requests
import time
import os
from kindletool import emailUtils
from kindletool.config import book_path, receivers

pwd_path = os.path.abspath(os.path.dirname(__file__))


def push_book():
    periodical = str(time.strftime("%Y-%m-%d"))
    filename = 'The_Economist_-_%s.mobi' % (periodical)
    url = 'https://raw.githubusercontent.com/nailperry-zd/The-Economist/master/%s/%s' % (
        periodical, filename)
    down = requests.get(url)
    if down.status_code == 200:
        with open(os.path.join(pwd_path, book_path, filename), 'wb')as code:
            code.write(down.content)
    else:
        print('%s不存在，请检查期数是否正确' % (filename))
    emailUtils.push_book(receivers, filename)


push_book()
