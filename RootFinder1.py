#!/usr/local/bin/python3

import numpy as np
#todo: I want to plot this whole thing visually, but a spreadsheet is good enough for now.
#import matplotlib.pyplot as plt
#xs = []     # x's is the x values of the data points to scatter plot
# Plot f(x)
#fxs = []    # y=f(x) values at each x point
import math
import random
random.seed()


class Polynomial(object):
    # degree is the highest degree (exponent) in the polynomial. For ex: x^4 + 2x^2 is degree 4
    def __init__(self, degree, maxCoefficient):
        self.degree = degree
        # self.coefficients is the coefficient numbers on each x term. coefficients[2] is
        # x^2 term, coefficients[1] is the x^1 term, [0] is the "constant" term (times x^0).
        self.coefficients = np.random.rand(self.degree + 1)
        # Now, coefficients holds floats ranging from 0.0 to 0.1. Instead, shift this to
        # the range of -maxCoefficient to maxCoefficient
        self.coefficients = (self.coefficients - 0.5) * (2 * maxCoefficient)

    # returns a string describing the polynomial like: "10x^3 -1.5x^2 + 99x - 45.5"
    def getDescription(self):
        result = ""
        bIsFirstTerm = True
        for i in range(self.degree, 0, -1):
            if bIsFirstTerm:
                bIsFirstTerm = False
            else:
                result = result + " + "
            #result = result + "{:.f}".format(self.coefficients[i]) + "x^" + str(i)
            result = result + str(self.coefficients[i]) + "x^" + str(i)
        # The loop above stopped before printing 0, which is a special case anyway
        #result = result + "{:.f}".format(self.coefficients[0])
        result = result + " + " + str(self.coefficients[0])
        return result

    # returns the value of this function evaluated at x
    def evalAt(self, x):
        result = self.coefficients[0]
        for i in range(1, self.degree + 1):
            result = result + self.coefficients[i] * (x ** i)
        return result

# Here's an example Polynomial for the function in HW8: -1*x**3 + 10*x + 15
#hw8Poly = Polynomial(3, 1.0)
#hw8Poly.coefficients = [15.0, 10.0, 0.0, -1.0]
#print("HW8 poly looks like: " + hw8Poly.getDescription())

def fFromDay8(x):
    #This approximates the function in worksheet 8, a discontinuous graph
     if x <= 3.6875:
         return 5
     else:
         return -5


### Declare input parameters from the user
a_1 = 3.0      # Initial value of left edge to search from
b_1 = 4.0      # Initial value of right edge to search to
k = 3           # number of base-10 digits to find
f = fFromDay8   # f is the function we'll evaluate in this root approximation algorithm
### End declaration of user input parameters


# Initialize a few variables needed for the bisection algorithm
if a_1 >= b_1:
    print("a_1 must be less than b_1")
    exit(0)
a = a_1
b = b_1
minimumDeltaX = 1.0 / (2 * 10**k)  # 1/2 of the decimal place we care about
# Print column headers
print("n Step   a left    f(a) b right  f(b) c mid     f(c) a-b delta" +
      "   error in f")
kMaxIterations = 50


for n in range(1, kMaxIterations):
    f_a_n = f(a)
    f_b_n = f(b)
    c = (b + a)/2
    f_c_n = f(c)
    deltaX = (b - a)

    rowData = (n,
               a, f_a_n,
               b, f_b_n,
               c, f_c_n,
               deltaX, abs(f_a_n) + abs(f_b_n))
    print("%6d  % 1.7f  % 2.2f  % 1.7f  % 2.2f  %1.8f  % 2.2f  %1.7f  % 2.2f" %
          rowData)

    # Advance to the next step by moving either a or b closer to each other
    if deltaX < minimumDeltaX:
        print("Exiting after finding " + str(k) + " matching digits...")
        break
    else:
        # Move either b+1 or a+1 to c, depending on which one's sign matches f(c)
        if f_c_n >= 0:
            if f_a_n >= 0:
                a = c
            else:
                if f_b_n >= 0:
                    b = c
                else:
                    print("Something went wrong because both f(a) < 0 and f(b) < 0")
                    break
        else:   # f_c_n < 0:
            if f_a_n < 0:
                a = c
            else:
                if f_b_n < 0:
                    b = c
                else:
                    print("Something went wrong because both f(a) >= 0 and f(b) >=  0")
                    break


# For this class, we want to show "k correct digits", which is not quite
# the same as rounding down. Here, we display extra digits and then truncate,
# which is very close to the correct thing.
cAsInt = math.floor(c) if (c > 0) else math.ceil(c)
cDecimals = abs(c - cAsInt)
cDecimalsAsString = "{:.20}".format(cDecimals)
cAsString = str(cAsInt) + cDecimalsAsString[1:k+2]
print("The approximate root is " + cAsString)
