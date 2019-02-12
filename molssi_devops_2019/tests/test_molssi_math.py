"""
Unit and regression test for the molssi_devops_2019 package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys



@pytest.fixture
def num_list_3():
    return [1,2,3,4,5]



@pytest.mark.parametrize("num_list, expected_mean",[
    ([1,2,3,4,5],3),
    ([0,2,4,6],3),
    ([1,2,3,4], 2.5),
    (list(range(1,100000)), 100000/2)])
def test_many(num_list, expected_mean):
    assert md.mean(num_list) ==  expected_mean

@pytest.mark.parametrize("x",[0,1])
@pytest.mark.parametrize("y",[2,3])
def test_foo(x,y):
    pass

def test_mean(num_list_3):
    """Sample test, will always pass so long as import statement worked"""
    observed = md.mean(num_list_3)
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


