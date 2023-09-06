#String method - starts with & ends with

s = 'python is very easy'

#startswith
print(s.startswith('python'))
print(s.startswith('py'))
print(s.startswith('is'))
print(s.startswith('is',7))

#endswith
print(s.endswith('easy'))
print(s.endswith('y'))
print(s.endswith('is'))
print(s.endswith('is',0,9))

#removesuffix & removeprefix
a ='python programming'
print(a.removeprefix('py'))
print(a.removeprefix('python'))
print(a.removesuffix('ing'))
print(a.removesuffix('programming'))

#spartition & rpartition
b = 'my name is arun'

print(b.partition('name'))
print(b.partition('n'))
print(b.partition('is'))

print(b.rpartition('name'))
print(b.rpartition('n'))
print(b.rpartition('s'))
print(b.rpartition('a'))