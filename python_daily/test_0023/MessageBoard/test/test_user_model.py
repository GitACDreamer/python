# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 15:08:31
# @title:  unittest user and model

import unittest
from .import create_app , session
from .import User


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        session.create_all()

    def tearDown(self):
        session.remove()
        session.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        user = User(password='test')
        self.assertTrue(user.password is not None)

    def test_no_password_getter(self):
        user = User(password='test')
        with self.assertRaises(AttributeError):
            user.password_hashed

    def test_password_verification(self):
        user = User(password='test')
        self.assertTrue(user.verify_password('test'))
        self.assertFalse(user.verify_password('tesd'))

    def test_password_salt_are_random(self):
        u1 = User(password='test')
        u2 = User(password='test')
        self.assertTrue(u1.password != u2.password)
