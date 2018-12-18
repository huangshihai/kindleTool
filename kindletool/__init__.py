from .config import mail_host, mail_user, mail_pass, sender, file_path
from .emailUtils import EmailUtil
from .epubee import Epubee

emailUtils = EmailUtil(file_path=file_path,
                       mail_host=mail_host,
                       mail_user=mail_user,
                       mail_pass=mail_pass,
                       sender=sender)
epubee = Epubee(file_path)
sendEmail = emailUtils.send_email
updateProxy = epubee.update_proxy
searchBook = epubee.get_search_list
addBook = epubee.add_book
delBook = epubee.del_book
downloadBook = epubee.download
