# Task 4: Floating-Point Arithmetic and Numerical Errors

## Inputs and mathematical operations

Part 1: The inputs are 0.1, 0.2 and 0.3. The program adds 0.1 and 0.2, then checks whether the result equals 0.3, first with an exact comparison and then with np.isclose().

Part 2: The inputs are the true value of the square root of 2 (about 1.41421356) and the approximation 1.414. The program calculates absolute error (true value minus approximate value, ignoring the sign) and relative error (absolute error divided by the true value).

Part 3: The inputs are small values of x (0.0001, 0.00000001 and 0.000000000001). The program calculates the same quantity with two formulas: the direct formula (sqrt(1+x) - 1) / x and the stable formula 1 / (sqrt(1+x) + 1).