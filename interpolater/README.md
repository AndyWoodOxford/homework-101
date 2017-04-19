# interpolator

Command line tool that reads in a two-dimensional matrix with non-adjacent
missing values and then outputs a matrix with no missing values.

The input and outputs are comma-separated files, with the former specifying missing values as 'nan'. 

## Features
Missing values are interpolated as the average of all neighbouring non-diagonal values.

## Future Releases
 * handling of adjacent missing values
