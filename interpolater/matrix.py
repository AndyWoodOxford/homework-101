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

    def __init__(self, missing_designator = None):
        ''' Creates an empty Matrix'''
        self.raw_data = []
        self.converted = []
        self.interpolated = []
        self.missing_designator = missing_designator
        self.missing_values = []
        self.rowcount = 0
        self.colcount = 0

    def get_dimensions(self):
        ''' Returns row and column count as a tuple '''
        return (self.rowcount, self.colcount)

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
        ''' Validates the input data. Raises a ValidationError upon failure. '''

        # get row count
        self.rowcount = len(self.raw_data)

        # check for empty cells and mismatched column counts
        column_count = 0 if self.rowcount == 0 else len(self.raw_data[0])
        for row in range(1, self.rowcount):
            count = len(self.raw_data[row])
            if column_count != count:
                raise errors.ValidationError('Mismatched column counts: {0}, {1}'.format(column_count, count))
            for col in range(count):
                cell = self.raw_data[row][col]
                if len(cell) == 0:
                    raise errors.ValidationError('Empty cell at ({0},{1})'.format(row, col))

        self.colcount = column_count

        if trace: print 'TRACE input matrix has {0} rows and {1} columns'.format(self.rowcount, self.colcount)


    def convert(self, trace=False):
        ''' Converts entries to numerical values. Handles an indicator for missing values. '''

        try:
            for i in range(self.rowcount):
                row = self.raw_data[i]
                row_converted = []
                for j in range(len(row)):
                    value = self.raw_data[i][j]

                    # record missing values as 'nan'
                    if self.missing_designator and value == self.missing_designator:
                        if trace: print 'TRACE missing value \'{0}\'found at ({1},{2})'.format(value, i,j)
                        row_converted.append(float('nan'))
                    else:
                        row_converted.append(float(value))

                self.converted.append(row_converted)

        except ValueError as e:
            raise errors.ValidationError('Non-numerical value at {0}, {1}'.format(i,j))

        if trace: print 'TRACE converted data: ', self.converted

    def find_missing_values(self, trace=False):
        '''
        Finds missing values. Traverses the raw data for the designated missing value symbol.
        '''
        for i in range(self.rowcount):
            for j in range(len(self.raw_data[i])):
                value = self.raw_data[i][j]

    def interpolate(self, trace=False):
        ''' Interpolates missing values '''

        # identify the locations (co-ordinates) of the missing values
        self.find_missing_values(trace)

        if trace: print 'TRACE missing values: ', self.missing_values

        return None

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
