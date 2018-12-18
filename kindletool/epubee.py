from bs4 import BeautifulSoup
import requests
import json
import random
import os

pwd_path = os.path.abspath(os.path.dirname(__file__))


class Epubee():
    def __init__(self, file_path):
        self.file_path = os.path.join(pwd_path, file_path)
        self.proxy = None
        self.cookie = {}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
        }

    def choiceIP(self, ip_pool):
        ip = random.choice(ip_pool)
        proxy = {'http': ip, 'https': ip}
        return proxy

    def update_proxy(self, proxy):
        self.proxy = proxy

    def getSessionid(self):
        login_url = 'http://cn.epubee.com'
        req = requests.get(login_url, headers=self.headers, proxies=self.proxy)
        str = req.headers['Set-Cookie']
        name, value = str.split(';')[0].split('=')
        return value

    def getCookie(self):
        print('开始获取cookie')
        self.cookie['ASP.NET_SessionId'] = self.getSessionid()
        url = 'http://cn.epubee.com//keys/genid_with_localid.asmx/genid_with_localid'
        data = {'localid': ''}
        response = requests.post(url, json=data, cookies=self.cookie, proxies=self.proxy)
        data = (json.loads(response.content.decode()))['d'][0]
        self.cookie['identify'] = data.get('ID')
        self.cookie['identifyusername'] = data.get('UserName')
        self.cookie['user_localid'] = data.get('Name')
        self.cookie['uemail'] = data.get('email')
        self.cookie['kindle_email'] = data.get('kindle_email')
        self.cookie['isVip'] = '1'
        self.cookie['leftshow'] = '1'

    def cookie_toString(self):
        cookie_str = ''
        for name, vlaue in self.cookie.items():
            cookie_str = cookie_str + str(name) + '=' + str(vlaue) + '; '
        return cookie_str

    def add_book(self, bookid):
        print('开始加入书本')
        uid = self.cookie.get('identify')
        cookie_str = self.cookie_toString()
        act = 'search'
        url = 'http://cn.epubee.com/app_books/addbook.asmx/online_addbook'
        data = {'bookid': bookid, 'uid': uid, 'act': act}
        header = {
            'Host': 'cn.epubee.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Cookie': cookie_str,
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive'
        }
        response = requests.post(url, headers=header, json=data, proxies=self.proxy)
        if response.status_code != 200:
            print('书本加入失败')
        else:
            print('书本加入成功')

    def del_book(self, bids=None):
        url = 'http://cn.epubee.com/app_books/deletemybooks.asmx/deletemybooks'
        uid = str(self.cookie.get('identify'))
        cookie_str = self.cookie_toString()
        if bids == None:
            books = self.getBookList()
            if len(books) > 0:
                bids = '0,'
                for book in books:
                    bids += book.get("bid") + ','
                    bids = bids[:-1]
        if bids != None:
            data = {'uid': uid, 'bids': bids}
            header = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Cookie': cookie_str,
                'Host': 'cn.epubee.com',
                'Origin': 'http://cn.epubee.com',
                'Referer': 'http://cn.epubee.com/files.aspx',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
                'X-Requested-With': 'XMLHttpRequest'
            }
            response = requests.post(url, headers=header, json=data, proxies=self.proxy)
            if response.status_code != 200:
                print('删除书本失败')
            else:
                print('删除书本成功')

    def getBookList(self):
        books = []
        uid = str(self.cookie.get('identify'))
        url = 'http://cn.epubee.com/files.aspx?userid=' + uid
        cookie_str = self.cookie_toString()
        header = {
            'Host': 'cn.epubee.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Cookie': cookie_str,
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'max-age=0 ',
        }
        req = requests.get(url, headers=header, proxies=self.proxy)
        if req.status_code == 200:
            bsObj = BeautifulSoup(req.text, 'html.parser')
            allbooks = bsObj.find_all('p', class_='allbooks')[0].find_all('a')[1].get_text().strip()
            books_count = allbooks[allbooks.rfind('[') + 1:-1]
            for i in range(int(books_count)):
                name = bsObj.find('span', {'id': 'gvBooks_lblTitle_' + str(i)}).get_text()
                format = bsObj.find('a', {'id': 'gvBooks_gvBooks_child_' + str(i) + '_hpdownload_0'}).get_text()
                filename = name + format
                bid = bsObj.find('span', {'id': 'gvBooks_gvBooks_child_' + str(i) + '_lblBID_0'}).get_text()
                books.append({'filename': filename, 'bid': bid})
            return books
        else:
            print('fail')
            return books

    def get_key(self, bid):
        url = 'http://cn.epubee.com/app_books/click_key.asmx/getkey'
        data = {'isVip': 1, 'uid': self.cookie.get('identify'), 'strbid': bid}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, json=data, proxies=self.proxy)
        dict = json.loads(response.content.decode())
        t_key = dict.get('d')[0]
        return t_key

    def download(self, filename, bid):
        filename = os.path.join(self.file_path, filename)
        cookie_str = self.cookie_toString()
        uid = str(self.cookie.get('identify'))
        t_key = self.get_key(bid)
        url = 'http://cn.epubee.com/getFile.ashx?bid=' + bid + '&uid=' + uid + '&t_key=' + t_key
        header = {
            'Host': 'cn.epubee.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Cookie': cookie_str,
            'Upgrade-Insecure-Requests': '1',
        }
        down = requests.get(url, headers=header, proxies=self.proxy)
        with open(filename, 'wb')as code:
            code.write(down.content)

    def get_search_list(self, key=None):
        dict = []
        if key == None:
            return dict
        url = 'http://cn.epubee.com/keys/get_ebook_list_search.asmx/getSearchList'
        data = {'skey': key}
        cookie_str = self.cookie_toString()
        header = {
            'Host': 'cn.epubee.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Cookie': cookie_str,
            'Upgrade-Insecure-Requests': '1',
        }
        response = requests.post(url, headers=header, json=data, proxies=self.proxy)
        if response.status_code == 200:
            dict = json.loads(response.content.decode())['d']
        return dict


if __name__ == '__main__':
    loc = 'E:\\资料\\电子书\\kindle\\'
    # 下载地址---F:\资料\电子书\kindle\   KxrbnqbpG9yIpkxWSozxtw%3d%3d
    # while(True):
    #
    #     try:
    #         # ip = random.choice(iplist)
    #         # proxy={'http':ip,'https':ip}
    #         # print('代理IP: %s', proxy.get('http'))
    #         getCookie()
    #         uid = str(cookie.get('identify'))
    #         print('用户：', uid)
    #         time.sleep(1)
    #        # bookid = str(input('请输入：'))
    #        # add_Book(cookie, bookid)
    #        # time.sleep(3)
    #         filename, bid = getBookList(cookie)
    #         print('开始下载', filename)
    #         download(filename,bid,cookie,loc)
    #         print('done!')
    #     except:
    #         user_input=input('请输入Enter结束操作,按c继续')
    #         if user_input=='\n':
    #             break
    #         elif user_input.lower()=='c':
    #             continue
    #         else:
    #             break

    # 获取图书测试
    # ip = random.choice(iplist)
    # proxy={'http':ip,'https':ip}
    # print('代理IP: %s', proxy.get('http'))
    # getCookie()
    # uid = str(cookie.get('identify'))
    # print('用户：', uid)
    # time.sleep(1)
    # del_books()
