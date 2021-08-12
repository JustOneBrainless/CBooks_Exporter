from data.testdata.api_key import MY_API_KEY
from src.requester.constants import *
from src.requester.requester import Requester


class Exporter(object):

    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books
        self.requester = Requester(MY_API_KEY)

    def create_files(self):
        # TODO Books[] to flat file in ISO 8859-1 as .txt
        # TODO Pics of Books[] to zip archive
        books = [1, 2, 3, 4, 5]
        offers = open("offer.txt", "x")
        offers.close()
        with open("offer.txt", "w") as f:
            while books:
                f.write('\t'.join(books[1:]) + '\n')
        f.close()
        pass

    def export(self, pics, books):
        # TODO File upload
        self.requester.request(I_FILE_IMPORT, POST, books)
        self.requester.request(I_FILE_IMPORT, POST, pics)
        pass
