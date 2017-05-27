# -*- coding: utf-8 -*-

from .context import DBUtils

import unittest


class CheckArgumentsTypeTestSuite(unittest.TestCase):
    """Test cases for check arguments type"""

    def test_arguments_type_list(self):
        """Test arguments type"""
        db = DBUtils.DBUtils(None)

        given = [""]
        expected = True

        res = db.check_args_type(given)
        self.assertEqual(res, expected, "Argument's type not correctly detected")

    def test_arguments_type_dict(self):
        """Test arguments type"""
        db = DBUtils.DBUtils(None)

        given = {"aa": True}
        expected = True

        res = db.check_args_type(given)
        self.assertEqual(res, expected, "Argument's type not correctly detected")

    def test_arguments_type_string(self):
        """Test arguments type"""
        db = DBUtils.DBUtils(None)

        given = "bimbambidubidubi"
        expected = False

        res = db.check_args_type(given)
        self.assertEqual(res, expected, "Argument's type not correctly detected")
