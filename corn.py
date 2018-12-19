import kindletool
from kindletool.config import receivers
import os


def download():
    kindletool.downloadBooks()


def push():
    for root, dirs, files in os.walk(kindletool.books_path):
        for file in files:
            kindletool.sendEmail(receivers, file, file, file)
            os.remove(file)
download()