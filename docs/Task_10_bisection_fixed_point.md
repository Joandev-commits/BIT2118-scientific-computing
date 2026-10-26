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
## Modified real-world case: break-even point of a small shop

Program file: code/Task_10_break_even_case.py

### New assumptions
- A small shop sells mandazi at KES 60 each.
- Fixed costs (rent and equipment) are KES 5,000.
- Making one mandazi costs KES 20.
- An extra cost of 0.01 x (number sold)^2 stands for overtime and wear on the equipment when many are made.
- Everything that is made is sold.

### Input data
- Selling price: 60 KES
- Fixed cost: 5000 KES
- Cost per mandazi: 20 KES
- Extra cost factor: 0.01
- Bisection interval: from 0 to 1000 mandazi

### The mathematics
- Income = 60 x q, where q is the number of mandazi sold
- Cost = 5000 + 20q + 0.01q^2
- Profit = Income - Cost = 40q - 0.01q^2 - 5000
- The break-even point is the value of q where profit = 0. I used the bisection method to find it.

### Output

Profit at 0 sales: -5000.00 KES
Profit at 1000 sales: 25000.00 KES
Break-even quantity: 129.17 mandazi
Income at break-even: 7750.28 KES
Bisection iterations: 44

### Interpretation
With no sales, the shop loses its fixed costs of KES 5,000. With 1,000 sales, it makes a profit of KES 25,000. Profit changes from negative to positive, so bisection can find the point where it is zero. The break-even quantity is about 129.17 mandazi, where income of about KES 7,750 equals cost. Because the shop cannot sell part of a mandazi, it must sell at least 130 to make a profit. Below this number the shop makes a loss, and above it the shop makes a profit. The graph shows profit starting at -5,000, rising through zero at about 129 mandazi, and reaching 25,000 at 1,000 mandazi.

### Limitation
This model is simple. Because of the extra cost term, profit would eventually fall again at very large quantities, so the model should only be trusted for quantities in the range I tested.