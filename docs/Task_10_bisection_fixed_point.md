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
Bisection iterations: 38
Bisection needed 38 steps, while fixed-point iteration needed only 13 steps, so fixed-point was faster here.

Both methods gave the same equilibrium temperature of 27.525211 degrees C. Bisection found it by repeatedly halving the interval from 20 to 40. Fixed-point iteration found it by starting at 30 and repeating the formula, and it took 13 steps. The graph agrees with these numbers. The line crosses zero at about 27.5 degrees C.
## Changing the inputs

Experiment 1: I changed the starting guess of the fixed-point method from T = 30 to T = 20. The equilibrium temperature stayed at 27.525211 degrees C. The number of fixed-point iterations went up from 13 to 14. The bisection result did not change, because I did not change its interval (38 iterations both times). This shows that the starting guess does not change the answer. It only changes how many steps are needed to reach it.
Experiment 2: I changed the bisection interval from [20, 40] to [25, 30]. The equilibrium temperature stayed at 27.525211 degrees C. The number of bisection iterations dropped from 38 to 36. The fixed-point result did not change (13 iterations). Each step of bisection cuts the interval in half, and the new interval is one quarter of the old one, which saves two steps. A smaller starting interval needs fewer steps, but the answer is the same as long as the root is still inside the interval.
Experiment 3: I changed the bisection interval to [30, 40]. The program stopped with the error "f(a) and f(b) must have different signs". At both 30 and 40 the heat-balance function is above zero, so there is no sign change and bisection cannot be sure that a root lies inside the interval. This shows that bisection only works when the starting interval has one end below zero and one end above zero.
## Meaning of the output

The program printed an equilibrium temperature of 27.525211 degrees C from both methods. This is the temperature at which heat gained equals heat lost. Because bisection and fixed-point iteration reached the same answer by different routes, I can be confident the answer is correct.

Bisection needed 38 iterations and fixed-point iteration needed 13. Bisection only halves the interval each time, so it is slow but very reliable, as long as the interval has a sign change. Fixed-point iteration moves closer to the answer faster here, but it only works when the rearranged formula settles down towards the root.

## Interpretation of the graph

The graph shows the heat-balance function for temperatures from 20 to 40 degrees C. The line starts below zero at 20 degrees C and rises steadily to above zero at 40 degrees C. It crosses zero at about 27.5 degrees C, and the dashed vertical line marks this point. Below this temperature the heat balance is negative, and above it the heat balance is positive. Because the line crosses zero only once, there is only one equilibrium temperature in this range.