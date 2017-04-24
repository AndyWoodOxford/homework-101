#!/usr/bin/env python

""" Unit tests for the Matrix class """

import os
import unittest

import matrix
import errors

class TestMatrix(unittest.TestCase):

    test_dir = os.path.join('tests', 'resources')

    def setUp(self):
        self.m = matrix.Matrix()

    # Reading the input data
    def test_no_such_file(self):
        testfile = 'nosuchfile.csv'
        infile = os.path.join(self.test_dir, testfile)
        try:
            self.m.read(infile)
        except IOError:
            pass
        else:
            self.fail('IOError not raised')

    def test_happy_case(self):
        testfile = 'complete_3_by_3.csv'
        infile = os.path.join(self.test_dir, testfile)
        self.m.read(infile)
        self.m.validate()
        self.assertEqual(self.m.get_dimensions(), (3,3))

    # Validating
    def test_mismatch_column_count(self):
        testfile = 'mismatch_column_counts.csv'
        infile = os.path.join(self.test_dir, testfile)
        try:
            self.m.read(infile)
            self.m.validate()
        except errors.ValidationError:
            pass
        else:
            self.fail('ValidationError not raised')

    def test_empty_file(self):
        testfile = 'empty.csv'
        infile = os.path.join(self.test_dir, testfile)
        self.m.read(infile)
        self.m.validate()
        self.assertEqual(self.m.get_dimensions(), (0,0))

    # Converting
    def test_bad_value(self):
        testfile = 'bad_value.csv'
        infile = os.path.join(self.test_dir, testfile)
        try:
            self.m.read(infile)
            self.m.validate()
            self.m.convert('nan')
        except errors.ValidationError:
            pass
        else:
            self.fail('ValidationError not raised')

    # Interpolating
    def test_adjacent_missing_row(self):
        testfile = 'missing_adjacent_row.csv'
        infile = os.path.join(self.test_dir, testfile)
        try:
            self.m.read(infile)
            self.m.validate()
        except errors.InterpolationError:
            pass
        else:
            self.fail('InterpolationError not raised')

    def test_adjacent_missing_col(self):
        testfile = 'missing_adjacent_col.csv'
        infile = os.path.join(self.test_dir, testfile)
        try:
            self.m.read(infile)
            self.m.validate()
        except errors.InterpolationError:
            pass
        else:
            self.fail('InterpolationError not raised')


    # Writing the results

if __name__ == '__main__':
    unittest.main()
