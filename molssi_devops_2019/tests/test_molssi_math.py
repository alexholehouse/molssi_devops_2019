"""
Unit and regression test for the molssi_devops_2019 package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys

def test_mean():
    """Sample test, will always pass so long as import statement worked"""
    num_list = [1,2,3,4,5]
    observed = md.mean(num_list)
    expected = 3

    assert(observed == expected)



#@pytest.mark.skip
@pytest.mark.my_test
def test_mean_type_error_string():
    """Sample test, will always pass as the function cannot compute average of string list """

    str_list=['a','b','c','d']
    with pytest.raises(TypeError):
        md.mean(str_list)

def test_mean_type_error():
    """Sample test, will always pass so long as import statement worked"""

    instring = 'abcdefg'
    with pytest.raises(TypeError):
        md.mean(instring)

def test_mean_zero_division_error():
    """Sample test, will always pass so long as import statement worked"""

    test_list = []
    with pytest.raises(ZeroDivisionError):
        md.mean(test_list)


