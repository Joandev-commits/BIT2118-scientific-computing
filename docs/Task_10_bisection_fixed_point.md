# Task 10: Root Finding - Bisection and Fixed-Point Methods

## Inputs and mathematical operations

The problem: find the temperature T at which heat gained equals heat lost. We write this as a function f(T) = T - 25 - 10*exp(-T/20). The answer is the value of T where f(T) = 0. This value is called a root.

### Method 1: Bisection

Inputs:
- The function f(T) = T - 25 - 10*exp(-T/20)
- The starting interval from 20 to 40 degrees C
- A tolerance of 1e-10, which tells the program when to stop

What the computer does:
- It checks that f(20) is negative (about -8.68) and f(40) is positive (about 13.65). A sign change means a root lies between them.
- It takes the middle of the interval and checks the sign of f there.
- It keeps the half that still has the sign change and throws away the other half.
- It repeats this until the interval is smaller than the tolerance.

### Method 2: Fixed-point iteration

Inputs:
- The rearranged equation g(T) = 25 + 10*exp(-T/20), which comes from T = g(T)
- A starting guess of T = 30
- A stopping rule: stop when two guesses differ by less than 1e-10
- A limit of 100 iterations

What the computer does:
- It puts the current guess into g(T) to get a new guess.
- It repeats, using each new answer as the next guess.
- It stops when the guess stops changing.

### The graph

The program also plots f(T) for temperatures from 20 to 40. The point where the line crosses zero is the equilibrium temperature. The program saves this graph as docs/Task_10_graph.png.
## Original output

When I ran the program, it printed:

Bisection equilibrium temperature: 27.525211 C
Fixed-point equilibrium temperature: 27.525211 C
Fixed-point iterations: 13

Both methods gave the same equilibrium temperature of 27.525211 degrees C. Bisection found it by repeatedly halving the interval from 20 to 40. Fixed-point iteration found it by starting at 30 and repeating the formula, and it took 13 steps. The graph agrees with these numbers. The line crosses zero at about 27.5 degrees C.