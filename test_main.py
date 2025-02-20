from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(5)) == 4 * 5
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(10)) == 0 * 10
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8 * 8
    assert quadratic_multiply(BinaryNumber(1234), BinaryNumber(5678)) == 1234 * 5678


test_multiply()
