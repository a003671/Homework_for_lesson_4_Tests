from unittest import TestCase

from yandex_API import MyYandexDisk
from xxx import token


class TestYandexApi(TestCase):
    def setUp(self):
        self.datas = ('Test', 'MyDocument')
        self.result = 201
    
    def test_creating_folder(self):
        md = MyYandexDisk(token)
        for data in self.datas:
            result = md.creating_folder(data)
            self.assertEqual(result, self.result)
         