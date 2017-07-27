# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 15:02:59
# @title:  unit basic test

import unittest
from flask import current_app
from . import create_app, session


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        session.create_all()

    def tearDown(self):
        session.session.remove()
        session.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertFalse(current_app.config['TESTING'])
