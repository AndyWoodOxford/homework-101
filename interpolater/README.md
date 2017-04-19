# interpolator

Command line tool that reads in a two-dimensional matrix with non-adjacent
missing values and then outputs a matrix with no missing values.

The input and outputs are comma-separated files, with the former specifying missing values as 'nan'.

## Features
Missing values are interpolated as the average of all neighbouring non-diagonal values.

### Notes on Behaviour
There is no explicit requirement on the precision of the output matrix. Here, we have retained the precision of the values in the input file.

## Future Releases
 * handling of adjacent missing values
 * allow option of specifying the output precision
