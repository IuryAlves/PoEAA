#!/usr/bin/env python
# coding: utf-8


import os
import glob
import doctest
import unittest
import sys

from factories import product_factory

def setup():
    database_files = glob.glob('*.db')
    for database_file in database_files:
        os.remove(database_file)


if __name__ == '__main__':

    setup()

    # find all files that are in a folder and ends with .md
    files = glob.glob('**/*.md')
    print(files)
    # create the test suite
    tests = doctest.DocFileSuite(*files, globs={'Product': product_factory()})

    # run the tests
    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)
