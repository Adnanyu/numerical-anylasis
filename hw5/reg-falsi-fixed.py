import math

def f(x):
    return x**2 - 0.47 * x ** (1/2) - 1.90

a = 1.0
b = 2.0
epsilon = 10**(-5)

# The iteration function.
if f(a)*math.pow(f(a), 2) < 0:
    g = lambda x: (b*f(x) - x*f(b)) / (f(x) - f(b))
    prev_p = a
# p_n and b bracket the root
else:
    g = lambda x: (a*f(x) - x*f(a)) / (f(x) - f(a))
    prev_p = b
# a and p_n bracket the root

RE = 1
n = 1
Digits = 7
while RE >= epsilon:
    p = g(prev_p)
    RE = abs((p - prev_p) / p)
    print(n,"\t||\t", round(prev_p,5),"\t||\t", round(p,5),"\t||\t", RE)
    prev_p = p
    n += 1
    if n > 100:
        break

print('Approximation of the root is', p)
