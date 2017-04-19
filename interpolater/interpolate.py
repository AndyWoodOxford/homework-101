#!/usr/bin/env python

'''
Reads a dimensional matrix with non-adjacent missing values and outputs a matrix
with no missing values.
'''

import argparse
import csv
import sys

def main():
    # handle command-line arguments
    parser = argparse.ArgumentParser(description='2-D Matrix Interpolator')
    parser.add_argument('input', metavar='File', help='Input CSV file')
    parser.add_argument('-o', '--output', action='store', dest='out_file',
         default = sys.argv[0] + '.out', help='Output file for interpolated matrix')
    args = parser.parse_args()

    # create and popluate a Matrix with the raw input data
    try:
        matrix = Matrix()
        #matrix.read()
    except Exception e:
        print 'Ooops, something went wrong:', e
        exit 1

if __name__ == '__main__':
    main()
