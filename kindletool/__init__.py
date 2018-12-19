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
pushBook = epubee.add_push_book
downloadBooks = epubee.batch_download_books
books_path = epubee.book_path