# pip install pytest-order
import pytest
@pytest.mark.order(1)
def test_login():
    print("this is login")
def test_addtocart(before="test_checkout"):
    print("this is addtocart")
def test_checkout(after="test_addtocart"):
    print("this is checkout")

    ''' if we change the arrangement of these functions they will be executed
    in the order they are mentioned because of dependency
    '''