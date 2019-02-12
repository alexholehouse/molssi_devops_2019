"""
Unit and regression test for the molssi_devops_2019 package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys


def test_return_string():
    assert(isinstance(md.string_utils.title_case('yesh yesh yesh') ,str), True)
    #md.string_utils.title_case('yesh yesh yesh') ,str), T
