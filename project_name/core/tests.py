# -*- coding: utf-8 -*-

from django.test import TestCase


class CoreTestCase(TestCase):
    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
