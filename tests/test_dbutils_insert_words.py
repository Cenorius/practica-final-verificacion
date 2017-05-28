# -*- coding: utf-8 -*-

from .context import DBUtils

import mock
import unittest
from test_auxiliary_functions import get_fake_collection

class InsertWordsTestSuite(unittest.TestCase):
      def test_exists_in_database(self):
        self.assertTrue(True)