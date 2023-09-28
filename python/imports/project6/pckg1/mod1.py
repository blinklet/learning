def fun1():
    print("fun1")

from . import mod2

mod2.fun2()

from pckg2 import mod1p

mod1p.fun1p()