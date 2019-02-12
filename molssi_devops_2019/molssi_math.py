"""
molssi_math.py
A sample repo for the workshop what we did in january 2019 at VT

Handles the primary functions
"""

import numbers


def mean(num_list):
    """
    Computes the mean of a list of numbers.

    Parameters
    -------
    num_list : iterable of numerical values
       List of numerical values

    Returns
    -------
    mean_val : float
       Average value (geometric mean)



    """

    # check list - this is restrictive, chec
    #if not isinstance(num_list, list):
    #    raise TypeError('Invalid input [%s] - input must be a list'%(num_list))

    # check you can iterate through (gives set/numpy compatibility)
    try:
        some_object_iterator = iter(num_list)
    except TypeError as te:
        raise TypeError('Invalid input [%s] - input must be iterable' % (num_list))

    # check
    if len(num_list) == 0:
        raise ZeroDivisionError('Cannot calculate meean of empty list')

    total = 0
    for i in num_list:
        if not isinstance(i, numbers.Number):
            raise TypeError('One or more of values in iterable was not a number')

        total = total + i

    return total / len(num_list)


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
