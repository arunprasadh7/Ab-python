# 11 Challenge  Flattening Nested List

def flatten(L):
    for i in L:
        if hasattr(i, '__iter__'):
            yield from flatten(i)
        else:
            yield i


f = flatten([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

g = flatten([1, 2, [3, [4, 5], 6, 7], 8])
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))