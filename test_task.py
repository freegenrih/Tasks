#!/usr/bin/python
import unittest
import json

from requests import get, put, delete, post

BASE_URL = 'http://localhost:5000/'

class TestUM(unittest.TestCase):
    json_string = str(get(BASE_URL).json()).replace('\'', '\"')
    parsed_json = json.loads(json_string)
    token = parsed_json['master_token']

    def test_1(self):
        self.assertEqual(str(get(BASE_URL)), '<Response [200]>')

    def test_2(self):
        self.assertEqual(str(get(BASE_URL+'tasks')), '<Response [401]>')

    def test_3(self):
        self.assertEqual(str(get(BASE_URL+'tasks/task1')), '<Response [401]>')

    def test_4(self):
        self.assertEqual(str(get(BASE_URL+'tasks/task2')), '<Response [401]>')

    def test_5(self):
        self.assertEqual(str(get(BASE_URL+'tasks/task3')), '<Response [401]>')

    def test_6(self):
        self.assertEqual(str(post(BASE_URL+'tasks/', data={'task': 'new task'})), '<Response [404]>')

    def test_7(self):
        self.assertEqual(str(delete(BASE_URL+'tasks/task1')), '<Response [401]>')

    def test_8(self):
        self.assertEqual(str(delete(BASE_URL+'tasks/task2')), '<Response [401]>')

    def test_9(self):
        self.assertEqual(str(delete(BASE_URL+'tasks/task3')), '<Response [401]>')

    def test_10(self):
        self.assertEqual(str(put(BASE_URL+'tasks/task1', data={'task': 'new_1 task'})), '<Response [401]>')

    def test_11(self):
        self.assertEqual(str(put(BASE_URL+'tasks/task2', data={'task': 'new_2 task'})), '<Response [401]>')

    def test_12(self):
        self.assertEqual(str(put(BASE_URL+'tasks/task3', data={'task': 'new_3 task'})), '<Response [401]>')

    def test_13(self):
        self.assertEqual(
            str(put(BASE_URL+'tasks/task1',
                    data={'master_token': self.token, 'task': 'new_1 task'})), '<Response [201]>')

    def test_14(self):
        self.assertEqual(
            str(put(BASE_URL+'tasks/task2',
                    data={'master_token': self.token, 'task': 'new_2 task'})), '<Response [201]>')

    def test_15(self):
        self.assertEqual(
            str(put(BASE_URL+'tasks/task3',
                    data={'master_token': self.token, 'task': 'new_3 task'})), '<Response [201]>')

    def test_16(self):
        self.assertEqual(
            str(post(BASE_URL+'tasks',
                     data={'master_token': self.token, 'task': 'new_4 task'})), '<Response [201]>')

    def test_17(self):
        self.assertEqual(
            str(post(BASE_URL+'tasks',
                     data={'master_token': self.token, 'task': 'new_5 task'})), '<Response [201]>')

    def test_18(self):
        self.assertEqual(
            str(post(BASE_URL+'tasks',
                     data={'master_token': self.token, 'task': 'new_6 task'})), '<Response [201]>')

    def test_19(self):
        self.assertEqual(
            str(put(BASE_URL+'tasks/task4',
                    data={'master_token': self.token, 'task': 'new_4 task'})), '<Response [201]>')

    def test_20(self):
        self.assertEqual(
            str(put(BASE_URL+'tasks/task5',
                    data={'master_token': self.token, 'task': 'new_5 task'})), '<Response [201]>')

    def test_21(self):
        self.assertEqual(
            str(put(BASE_URL+'tasks/task6',
                    data={'master_token': self.token, 'task': 'new_6 task'})), '<Response [201]>')

    def test_22(self):
        self.assertEqual(
            str(delete(BASE_URL+'tasks/task4',
                       data={'master_token': self.token})), '<Response [204]>')

    def test_23(self):
        self.assertEqual(
            str(delete(BASE_URL+'tasks/task5',
                       data={'master_token': self.token})), '<Response [204]>')

    def test_24(self):
        self.assertEqual(
            str(delete(BASE_URL+'tasks/task6',
                       data={'master_token': self.token})), '<Response [204]>')

    def test_25(self):
        self.assertEqual(str(get(BASE_URL+'tasks',data={'master_token': self.token})), '<Response [200]>')


if __name__ == '__main__':
    unittest.main()
