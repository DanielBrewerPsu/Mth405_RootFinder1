#!/usr/local/bin/python3

#import numpy as np
#todo: I want to plot this whole thing visually, but a spreadsheet is good enough for now.
#import matplotlib.pyplot as plt
#xs = []     # x's is the x values of the data points to scatter plot
# Plot f(x)
#fxs = []    # y=f(x) values at each x point


def f(x):
    #return -1*x**3 + 10*x + 15 # The function in HW8

    #This approximates the function in worksheet 8, a discontinuous graph
    if x <= 3.6875:
        return 5
    else:
        return -5


# Initialize search parameters
a_1 = 3.5     # Initial value of left edge to search from
b_1 = 4.0    # Initial value of right edge to search to
if a_1 >= b_1:
    print("a_1 must be less than b_1")
    exit(0)
a_n = a_1
b_n = b_1
k = 3       # Number of digits to get to match
minimumDeltaX = 1.0 / (2 * 10**(k + 1)) # 1/2 of the decimal place we care about

# Print column headers
print("n Step   a_n left    f(a_n) b_n right  f(b_n) c_n mid      f(c_n) a-b delta" +
      "  error in f")

kMaxIterations = 50
for n in range(1, kMaxIterations):
    f_a_n = f(a_n)
    f_b_n = f(b_n)
    c_n = (b_n + a_n)/2
    f_c_n = f(c_n)
    deltaX = (b_n - a_n)

    rowData = (n,   \
        a_n, f_a_n, \
        b_n, f_b_n, \
        c_n, f_c_n, \
        deltaX, abs(f_a_n) + abs(f_b_n))
    print("%6d  % 1.7f  % 2.2f  % 1.7f  % 2.2f  %1.8f  % 2.2f  %1.7f  % 2.2f" %
          rowData)

    if deltaX < minimumDeltaX:
        print("Exiting after finding " + str(k) + " matching digits.")
        print(("The approximate root is {: 2." + str(k + 1) + "}").format(c_n))
        break
    else:
        # Move either b_n+1 or a_n+1 to c_n, depending on which one's sign matches f(c_n)
        if f_c_n >= 0:
            if f_a_n >= 0:
                a_n = c_n
            else:
                if f_b_n >= 0:
                    b_n = c_n
                else:
                    print("Something went wrong because both f(a_n) < 0 and f(b_n) < 0")
                    exit(2)
        else:   # f_c_n < 0:
            if f_a_n < 0:
                a_n = c_n
            else:
                if f_b_n < 0:
                    b_n = c_n
                else:
                    print("Something went wrong because both f(a_n) >= 0 and f(b_n) >=  0")
                    exit(2)

print("Stopping looking after " + str(n) + " iterations.")
print(("The approximate root is {: 2." + str(k + 1) + "}").format(c_n))
