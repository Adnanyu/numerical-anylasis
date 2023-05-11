import math
def f(x):
    return x * math.sin(1/x) + 0.05986

def XINT(u, v):
    return u - f(u)*(u - v)/(f(u) - f(v))

a = 0.06
b = 0.09
p = a  # to use in the first step
epsilon = 10**(-5)

n = 1
Digits = 7
while abs(f(p)) >= epsilon:
    p = XINT(a, b)
    print(n,"\t||\t", round(a,8),"\t||\t", round(p,8),"\t||\t", round(b,8),"\t||\t", round(f(a),11),"\t||\t", round(f(p),11))
    HotCold = f(a)*f(p)
    if HotCold < 0:
        b = p
    else:
        a = p
    n += 1

print('Approximation of the root is', p)
