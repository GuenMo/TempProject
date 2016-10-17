# coding:utf-8

"""
Created on 29 July 2016
@author: GuenMo-Kim
"""

def foo1(var1, var2, long_var_name='hi'):
    """
    This function does something.
    
    Parameters
    ----------
    var1 : array_like
        This is a type.
    var2 : int
        This is another var.
    Long_variable_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.
    
    Returns
    -------
    describe : type
        Explanation

    """
    pass

def foo2(va1, var2):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    print va1, var2
    
def foo3(va1, var2):
    """This function does something.
 
    :param name: The name to use.
    :type name: str.
    :param state: Current state to be in.
    :type state: bool.
    :returns:  int -- the return code.
    :raises: AttributeError, KeyError
    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]
 
    """
    print va1, var2

