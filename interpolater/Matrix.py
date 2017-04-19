#!/usr/bin/env python

import csv

class Matrix(object):
    ''' Represents a 2-D matrix containing numerical values.'''

    def __init__(self):
        self.raw_data = []
        self.interpolated = []
        self.precision = None

    def read(self, filename):
        ''' Reads in a 2-d matrix from a given filename.'''

        try:
            f = csv.reader(open(filename))
        except IOError as e:
            print 'Unable to open {} for reading: {}'.format(filename, e)
            raise
        finally:
            f.close()
