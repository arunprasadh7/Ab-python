# 6 Challenge  Inverting a Dictionary- convert keys to values and values to keys

def invert(d):
    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key

    return new_dict


d1 = {'a': 10, 'b': 20, 'c': 30}
nd1 = invert(d1)
print(f'Inverted dictionary is {nd1}.')
