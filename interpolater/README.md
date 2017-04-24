# interpolator

Command line tool that reads in a two-dimensional matrix with non-adjacent
missing values and then outputs a matrix with no missing values.

The input and outputs are comma-separated files, with the former specifying missing values as 'nan'.

**NB** Written against Python 2.7.11 on Mac OS.

## Status
Not operational.
  * need to solve the identification of adjacent values
  * fail if any neighbours of a missing value are also missing
  * populate interpolated matrix with either the existing value, or the average of its neighbours
  * write the interpolated matrix to the local filesystem  

## Usage

Run with the ''-h'' option.

## Features
Missing values are interpolated as the average of all neighbouring non-diagonal values.

### Notes on Behaviour
There is no explicit requirement on the precision of the output matrix. Here, we have retained the precision of the values in the input file.

## Future Releases
 * allow for missing and/or alternative missing value indicators
 * allow option of specifying the output precision*
 * handling of adjacent missing values
 *
