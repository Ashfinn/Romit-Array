'''
Finding the value of sin(x) with the following algorithm:
sin(x) = x^1/1! - x^3/3! + x^5/5! - x^7/7! + ..... + Infinity
It can be simplified to:

sin(x) = Σ ((-1)^n * x^(2 * n + 1) / (2 * n + 1)!)
where x => 0 to Infinity, n = accuracy (higher -> more precise)
'''
from math import factorial
n = int(input('n = ? : '))
x = int(input('x = ? : '))
for i in range(1,n):
    print(sum((-1)**n * x**(2 * n + 1) /factorial(2* n + 1)))
