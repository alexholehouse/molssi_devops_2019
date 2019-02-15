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




"""
@pytest.mark.parametrize("return_val, target_val, list_vals",[
    (-1, 3, []),
    (-1, 3, [1])])
"""
@pytest.mark.parametrize("return_val, target_val, list_vals",[
    (-1, 3, []),
    (-1, 3, [1]),
    (0,1, [1]),
    (0,1, [1, 3, 5]),
    (1,3, [1, 3, 5]),
    (2,5, [1, 3, 5]),
    (-1, 0, [1, 3, 5]),
    (-1, 2, [1, 3, 5]),
    (-1, 4, [1, 3, 5]),
    (-1, 6, [1, 3, 5]),
    (0,1, [1, 3, 5, 7]),
    (1,3, [1, 3, 5, 7]),
    (2,5, [1, 3, 5, 7]),
    (3,7, [1, 3, 5, 7]),
    (-1, 0, [1, 3, 5, 7]),
    (-1, 2, [1, 3, 5, 7]),
    (-1, 4, [1, 3, 5, 7]),
    (-1, 6, [1, 3, 5, 7]),
    (-1, 8, [1, 3, 5, 7])])
@pytest.mark.param
def test_many_chops(return_val, target_val, list_vals):    
    assert(return_val ==  md.chop(target_val, list_vals))




