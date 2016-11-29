#!/usr/bin/env python
# coding: utf-8


import glob
import doctest
import unittest
import sys

if __name__ == '__main__':

    # find all files that are in a folder and ends with .md
    files = glob.glob('**/*.md')

    # create the test suite
    tests = doctest.DocFileSuite(*files)

    # run the tests
    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)
