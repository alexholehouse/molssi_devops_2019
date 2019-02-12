"""
Unit and regression test for the molssi_devops_2019 package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys


def test_return_string():
    assert(isinstance(md.string_utils.title_case('yesh yesh yesh') ,str), True)


def test_return_s1():
    assert(md.string_utils.title_case('yeah') == 'Yeah')


def test_return_s2():
    assert(md.string_utils.title_case("yeah well that's just your opinion") == "Yeah Well That's Just Your Opinion")

def test_return_empty_string():
    with pytest.raises(TypeError):
        md.string_utils.title_case("")
    

@pytest.mark.parametrize("in_strings, out_strings",[
    ("yeah","Yeah"),
    ("yeah ok well fine", "Yeah Ok Well Fine"),
    ("WHY MUST YOU SHOUT","Why Must You Shout")])
def test_many(in_strings, out_strings):
    assert(md.string_utils.title_case(in_strings) == out_strings)
