#!/usr/bin/env python

'''
Reads a dimensional matrix with non-adjacent missing values and outputs a matrix
with no missing values.
'''

import argparse
import csv
import os
import sys

import matrix

def main():
    # handle command-line arguments
    parser = argparse.ArgumentParser(description='2-D Matrix Interpolator')
    parser.add_argument('infile', metavar='INFILE', help='Input CSV file')
    parser.add_argument('-o', '--output', action='store', dest='outfile',
        default = sys.argv[0] + '.out', help='Output file for interpolated matrix')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
        help='Verbose mode')
    args = parser.parse_args()

    # Workflow - read the input data, validate, interpolate and write the results
    try:
        m = matrix.Matrix()
        m.read(args.infile, trace=args.verbose)
        m.validate(trace=args.verbose)
        m.interpolate(trace=args.verbose)
        m.write(args.outfile, trace=args.verbose)
    except Exception as e:
        print 'Interpolation FAILED\n\tException caught:', e
        exit(1)

if __name__ == '__main__':
    main()
