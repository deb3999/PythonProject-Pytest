# pip install pytest-xdist

import pytest

def test_one():
    print("test one is running")
def test_two():
    print("test two is running")
def test_three():
    print("test three is running")
def test_four():
    print("test four is running")
# pytest .\pytestDirectory\test_parallel.py -v -s -n=2