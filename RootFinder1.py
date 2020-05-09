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


# Polynomial represents a polynomial function to find a root for
# Here's an example of creating the Polynomial for the function in HW8:
# -1*x**3 + (0*x**2) + 10*x + 15
# Instantiate one. 3 is the degree because x^3 is the highest term.
#hw8Poly = Polynomial(3, 1.0)
# Store the coefficients. They're from lowest-to-highest, the opposite of the standard order.
#hw8Poly.coefficients = [15.0, 10.0, 0.0, -1.0]
#print("HW8 poly looks like: " + hw8Poly.getDescription())
# And here's how to hand this polynomial to applyBisectionMethod:
#applyBisectionMethod(hw8Poly.evalAt)
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
        # The highest degree coefficient is special and cannot be 0
        while self.coefficients[self.degree] == 0.0:
            self.coefficients[self.degree] = random.randrange(-1 * maxCoefficient, maxCoefficient)

    # returns a string describing the polynomial like: "10x^3 -1.5x^2 + 99x - 45.5"
    def getDescription(self):
        result = ""
        bIsFirstTerm = True
        for i in range(self.degree, 0, -1):
            if self.coefficients[i] != 0:   # Skip "0" terms entirely
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


#fFromDay8 shows another way to define a function for applyBisectionMethod
def fFromDay8(x):
    #This approximates the function in worksheet 8, a discontinuous graph
     if x <= 3.6875:
         return 5
     else:
         return -5


k = 3           # number of base-10 digits to find
minimumDeltaX = 1.0 / (2 * 10**k)  # 1/2 of the decimal place we care about
kMaxIterations = 100     # A global const to ensure we don't search endlessly for a root


# applyBisectionMethod
# Returns a tuple: (wasSuccessful, [rowDataForEachStep])
# f the input parameter is the function to find a root for.
def applyBisectionMethod(f, a_1, b_1):
    rowDataList = []
    a = a_1
    b = b_1
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
        rowDataList.append(rowData)

        # Advance to the next step by moving either a or b closer to each other
        if deltaX < minimumDeltaX:
            #print("Exiting after finding " + str(k) + " matching digits...")
            return True, rowDataList
        else:
            # Move either b+1 or a+1 to c, depending on which one's sign matches f(c)
            if f_c_n >= 0:
                if f_a_n >= 0:
                    a = c
                else:
                    if f_b_n >= 0:
                        b = c
                    else:
                        #print("Something went wrong because both f(a) < 0 and f(b) < 0")
                        return False, rowDataList
            else:   # f_c_n < 0:
                if f_a_n < 0:
                    a = c
                else:
                    if f_b_n < 0:
                        b = c
                    else:
                        #print("Something went wrong because both f(a) >= 0 and f(b) >=  0")
                        return False, rowDataList


def printRowData(rowDataList):
    # Print column headers
    print("n Step    a left       f(a)    b right     f(b)    c mid        f(c)    a-b delta" +
          "    error in f")
    for rowData in rowDataList:
        print("%6d   % 1.7f   % 2.2f   % 1.7f   % 2.2f   %1.8f   % 2.2f   %1.7f   % 2.2f" %
              rowData)

def getStringWithKCorrectDigits(num):
    # For this class, we want to show "k correct digits", which is not quite
    # the same as rounding down. Here, we display extra digits and then truncate,
    # which is very close to the correct thing.
    numAsInt = math.floor(num) if (num > 0) else math.ceil(num)
    nonIntPart = abs(num - numAsInt)
    nonIntPartAsString = "{:.20}".format(nonIntPart)
    return str(numAsInt) + nonIntPartAsString[1:k+2]


# Apply these functions to a basic polynomial
poly = Polynomial(3, 1.0)
poly.coefficients = [15.0, 10.0, 0.0, -1.0]
print("The polynomial looks like: " + poly.getDescription())
results = (False, [])
while not results[0]:
    print("Applying bisection method")
    results = applyBisectionMethod(poly.evalAt, 3.0, 4.0)

printRowData(results[1])

c = results[1][-1][5]  # pull c from the last row
print("The approximate root is " + getStringWithKCorrectDigits(c))
