#!/usr/bin/env/python

import unittest
import sys

import login_check_test


__author__ = 'Dorota Filiczuk'


def suite():
    return unittest.TestSuite((
        unittest.makeSuite(login_check_test.login_check_test),

    ))


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    sys.exit(not result.wasSuccessful())