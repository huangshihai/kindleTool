import os
from .config import mail_host, mail_user, mail_pass, sender, book_path
from .epubee import Epubee
from kindletool import emailUtils

epubee = Epubee()
updateProxy = epubee.update_proxy
searchBook = epubee.get_search_list
downloadBook = epubee.download_book


def pushBook(filename, bookid, email):
    receivers = [email]
    book_path = os.path.join(epubee.book_path,  bookid + '_' + filename)
    if not os.path.exists(book_path):
        epubee.download_book(filename, bookid)
    emailUtils.push_book(receivers, filename)
