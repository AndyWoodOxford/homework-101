#!/usr/bin/env python

import csv
import errors
import math

class Matrix(object):
    ''' Represents a 2-D matrix containing numerical values.'''

    MISSING_VALUE = 'nan'

    @staticmethod
    def get_adjacent_values(matrix, rowpos, colpos, trace):
        '''
        Returns a list of non-diagonal adjacent values on a given location.

        TODO move to a utility module.
        TODO allow a range of adjacent values in each direction
        '''
        rowcount = len(matrix)

        if rowcount == 0:
            return

        colcount = len(matrix[0])

        adjacent = []
        for row in range(rowpos - 1, rowpos + 2):
            # row out-of-bounds
            if row < 0 or row >= rowcount:
                continue
            row_adjacent = []
            for col in range(colpos - 1, colpos + 2):
                # col out-of-bounds
                if col < 0 or col >= colcount:
                    continue
                # skip self
                if row == rowpos and col == colpos:
                    continue
                # skip adjacent diagonals
                if abs(rowpos - row) == 1 and abs(colpos - col) == 1:
                    continue
                row_adjacent.append(matrix[row][col])

            if len(row_adjacent) > 0: adjacent.append(row_adjacent)

        return adjacent

    def __init__(self):
        ''' Creates an empty Matrix'''
        self.raw_data = []
        self.converted = []
        self.interpolated = []
        self.missing = []
        self.rowcount = 0
        self.colcount = 0

    def read(self, filename, trace=False):
        ''' Reads a 2-D matrix from a given CSV. Note that all values are read as strings.'''

        try:
            with open(filename) as f:
                f_csv = csv.reader(f)
                row_num = 0
                self.raw_data = list(f_csv)
        except IOError as e:
            print 'Unable to open {} for reading: {}'.format(filename, e)
            raise

        if trace: print 'TRACE raw input', self.raw_data

    def validate(self, trace=False):
        ''' Validates the input data. Converts string values to floating points. '''

        # get row and column counts
        self.rowcount = len(self.raw_data)

        # short circuit for empty matrix
        if self.rowcount  == 0:
            self.colcount = 0
            return

        # check column count is consistent over each row
        count_first_row = len(self.raw_data[0])
        if self.rowcount == 1:
            self.colcount = count_first_row
        else:
            for row in range(1, self.rowcount):
                count = len(self.raw_data[row])
                if count != count_first_row:
                    raise errors.ValidationError('Mismatched row counts: {0}, {1}'.format(count_first_row, count))
            self.colcount = count_first_row

        if trace: print 'TRACE input matrix has {0} rows and {1} columns'.format(self.rowcount, self.colcount)

        # inspect each element - convert to floating point, record missing data
        try:
            for i in range(self.rowcount):
                row = self.raw_data[i]
                row_converted = []
                for j in range(len(row)):
                    value = self.raw_data[i][j]

                    # missing value - record location
                    if self.MISSING_VALUE == value:
                        if trace: print 'TRACE missing value found at ({0},{1})'.format(i,j)
                        self.missing.append((i,j))

                    # convert string value (including 'nan') to floating point
                    num = float(value)
                    row_converted.append(num)

                self.converted.append(row_converted)

        except ValueError as e:
            raise errors.ValidationError('Non-numerical value at {0}, {1}'.format(i,j))

        if trace: print 'TRACE converted data: ', self.converted
        if trace: print 'TRACE missing values: ', self.missing

    def interpolate(self, trace=False):
        ''' Interpolates missing values '''
        for i in range(self.rowcount):
            row = self.converted[i]
            row_interpolated = []
            for j in range(len(row)):
                value = self.converted[i][j]
                adjacent = self.get_adjacent_values(self.converted, i, j, trace)

                if trace: print 'adjacent to {0} at ({1}, {2}): {3}'.format(value, i, j, adjacent)

                # adjacent missing values are not supported
                if math.isnan(value):
                    pass

                # replace missing value with arithmetic average of adjacent values


    def write(self, filename, trace=False):
        ''' Writes interpolated matrix to an output file '''
        pass
