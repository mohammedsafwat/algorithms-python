__author__ = 'mohammadsafwat'
import timeit

def implementation1():
    l = []
    for i in range(1000):
        l += [i]

def implementation2():
    l = []
    for i in range(1000):
        l.append(i)

def implementation3():
    l = [i for i in range(0, 1000)]

def implementation4():
    l = list(range(1000))

t1 = timeit.Timer("implementation1()", "from __main__ import implementation1")
print("concatenation took ", t1.timeit(number=1000), "ms")

t2 = timeit.Timer("implementation2()", "from __main__ import implementation2")
print("append took ", t2.timeit(number=1000), "ms")

t3 = timeit.Timer("implementation3()", "from __main__ import implementation3")
print("list comprehension took ", t3.timeit(number=1000), "ms")

t4 = timeit.Timer("implementation4()", "from __main__ import implementation4")
print("range took ", t4.timeit(number=1000), "ms")

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print("popzero took ", popzero.timeit(number=1000), "ms")

x = list(range(2000000))
print("popend took ", popend.timeit(number=1000), "ms")

popzero = timeit.Timer("x.pop(0)",
                "from __main__ import x")
popend = timeit.Timer("x.pop()",
               "from __main__ import x")

#print("pop(0)   pop()")
#for i in range(1000000,100000001,1000000):
    #x = list(range(i))
    #pt = popend.timeit(number=1000)
    #x = list(range(i))
    #pz = popzero.timeit(number=1000)
    #print("%15.5f, %15.5f" %(pz,pt))


