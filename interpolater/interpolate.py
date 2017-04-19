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
    parser.add_argument('-o', '--output', action='store', dest='out_file',
         default = sys.argv[0] + '.out', help='Output file for interplated matrix')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
