"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    xvec = x.binary_vec
    yvec = y.binary_vec

    # Ensure both binary vectors have the same length by padding
    padded = pad(xvec, yvec)
    xvec = padded[0]
    yvec = padded[1]

    # Base case: if both numbers are small enough, return their product
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    # Split numbers into left and right halves
    mid = len(xvec) // 2
    x_left = split_number(xvec)[0]
    x_right = split_number(xvec)[1]
    y_left = split_number(yvec)[0]
    y_right = split_number(yvec)[1]

    # Recursive calls to compute intermediate products
    p1 = _quadratic_multiply(x_left, y_left)  # xL * yL
    p2 = _quadratic_multiply(x_right, y_right)  # xR * yR

    x_sum = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
    y_sum = BinaryNumber(y_left.decimal_val + y_right.decimal_val)
    p3 = _quadratic_multiply(x_sum, y_sum)

    # Compute result using formula:
    # xy = 2^n * p1 + 2^(n/2) * (p3 - p1 - p2) + p2
    term1 = bit_shift(p1, 2 * mid)  # 2^n * p1
    middle_term = BinaryNumber(p3.decimal_val - p1.decimal_val - p2.decimal_val)
    term2 = bit_shift(middle_term, mid)  # 2^(n/2) * (p3 - p1 - p2)

    result = BinaryNumber(term1.decimal_val + term2.decimal_val + p2.decimal_val)

    return result


def run_quadratic_multiply_test(x, y, f):
    x_bin = BinaryNumber(x)  # Convert x to BinaryNumber
    y_bin = BinaryNumber(y)  # Convert y to BinaryNumber

    start = time.time()  # Start timer
    result = f(x_bin, y_bin)  # Perform multiplication
    end = time.time()  # End timer

    return result.decimal_val, (end - start) * 1000  # Return product and execution time (ms)


    
    

