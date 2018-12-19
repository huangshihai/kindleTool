import os
from .config import mail_host, mail_user, mail_pass, sender, book_path
from .emailUtils import EmailUtil
from .epubee import Epubee

emailUtils = EmailUtil(file_path=book_path,
                       mail_host=mail_host,
                       mail_user=mail_user,
                       mail_pass=mail_pass,
                       sender=sender)
epubee = Epubee()
sendEmail = emailUtils.send_email
updateProxy = epubee.update_proxy
searchBook = epubee.get_search_list
downloadBook = epubee.download_book


def pushBook(filename, bookid, email):
    receivers = [email]
    book_path = os.path.join(epubee.book_path, filename)
    if os.path.exists(book_path):
        sendEmail(receivers, filename, filename, filename)
    else:
        epubee.download_book(filename, bookid)
        sendEmail(receivers, filename, filename, filename)
