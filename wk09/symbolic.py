# -*- coding: cp949 -*-
from sympy import *
a = Rational(1, 2)
print "a =", a

print "pi**2 =", pi**2

print "pi.evalf() =", pi.evalf()

print "pi + exp(1) =", pi + exp(1)

print "(pi + exp(1)).evalf() =", (pi + exp(1)).evalf()

print "oo =", oo

print "oo > 99999 =", oo > 99999

print "sqrt(2) =", sqrt(2).evalf(100)

print "1/2 + 1/3 =", Rational(1, 2) + Rational(1, 3)

F, r, sigma_max, sf = symbols('F r sigma_max safety_factor')

area = pi * r * r
sigma = F / area
solution = solve([sigma - sigma_max/sf], r)
print "solution =", simplify(solution)

'''2.10.1.3'''

x = Symbol('x')
y = Symbol('y')

print "x+y+x-y =", x+y+x-y

print "(x+y)**2 =", (x+y)**2

'''2.10.2.1'''

print "expand((x+y)**3) =", expand((x+y)**3)

print "expand(x+y, complex=True) =", expand(x+y,complex=True)

print "expand(cos(x+y), trig=True) =", expand(cos(x+y), trig=True)

'''2.10.2.2'''

print "simplify((x+x*y)/x) =", simplify((x+x*y)/x)

'''2.10.3.1'''
print "limit(sin(x)/x,x,0) =", limit(sin(x)/x, x, 0)

print "limit(x,x,oo) =", limit(x, x, oo)

print "limit(1/x,x,oo) =", limit(1/x, x, oo)

print "limit(x**x,x,0) =", limit(x**x, x, 0)

'''2.10.3.2'''

print "diff(sin(x), x) =", diff(sin(x), x)

print "diff(sin(2*x), x) =", diff(sin(2*x), x)

print "diff(tan(x), x) =", diff(tan(x), x)

print "limit((tan(x+y)-tan(x))/y,y,0) =", limit((tan(x+y)-tan(x))/y,y,0)

print "diff(sin(2*x), x, 1) =", diff(sin(2*x), x, 1)

print "diff(sin(2*x), x, 2) =", diff(sin(2*x), x, 2)

print "diff(sin(2*x), x, 3) =", diff(sin(2*x), x, 3)

'''2.10.3.3'''

print "series(cos(x), x) =", series(cos(x), x)

print "series(1/cos(x), x) =", series(1/cos(x), x)

