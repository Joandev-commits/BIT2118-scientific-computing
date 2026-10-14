# Task 4: Floating-Point Arithmetic and Numerical Errors

## Inputs and mathematical operations

Part 1: The inputs are 0.1, 0.2 and 0.3. The program adds 0.1 and 0.2, then checks whether the result equals 0.3, first with an exact comparison and then with np.isclose().

Part 2: The inputs are the true value of the square root of 2 (about 1.41421356) and the approximation 1.414. The program calculates absolute error (true value minus approximate value, ignoring the sign) and relative error (absolute error divided by the true value).

Part 3: The inputs are small values of x (0.0001, 0.00000001 and 0.000000000001). The program calculates the same quantity with two formulas: the direct formula (sqrt(1+x) - 1) / x and the stable formula 1 / (sqrt(1+x) + 1).
## Changing the inputs

Experiment 1: I changed the approximate value of the square root of 2 from 1.414 to 1.41421. The absolute error dropped from 0.00021356 to 0.00000356, and the relative error dropped from 0.0151% to 0.000252%. A more accurate approximation gives a smaller error.

Experiment 2: I added a smaller value of x (1e-15) to the list. The direct formula gave 0.444089209850, which is far from the correct value of 0.5. The stable formula still gave 0.5. This shows that the direct formula loses accuracy as x gets smaller, while the stable formula does not.

## Meaning of the output

Part 1: The program printed 0.30000000000000004 for 0.1 + 0.2. The exact comparison returned False and np.isclose() returned True. This happens because the computer stores numbers in binary, and 0.1 cannot be stored exactly. The stored value is very slightly off. For real work, we should compare numbers with a tolerance, not with exact equality.

Part 2: Using 1.414 instead of the square root of 2 gives an absolute error of 0.00021356 and a relative error of 0.0151%. The mistake is real, but it is very small compared to the size of the number.

Part 3: The direct formula loses accuracy as x gets smaller. At x = 1e-15 it gave 0.444089209850 instead of 0.5. The reason is that it subtracts 1 from a number that is almost exactly 1, which wipes out most of the correct digits. The stable formula avoids that subtraction, so it stayed at 0.5 every time. This shows that the choice of formula matters on a computer.
| Approximation | Absolute error | Relative error |
|---|---|---|
| 1.4 | 0.01421356 | 1.00505063% |
| 1.414 (original) | 0.00021356 | 0.01510114% |
| 1.41421 | 0.00000356 | 0.00025190% |

| x | Direct formula | Stable formula |
|---|---|---|
| 1e-04 | 0.499987500624 | 0.499987500625 |
| 1e-08 | 0.499999996961 | 0.499999998750 |
| 1e-12 | 0.500044450291 | 0.500000000000 |
| 1e-15 | 0.444089209850 | 0.500000000000 |