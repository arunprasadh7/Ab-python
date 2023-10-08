# 9 Challenge  Minimum Variable Number

# when low limit is none
def minimum(*values, low_limit=None):
    if low_limit is None:
        minimum_number = min(values)
    return minimum_number


print(minimum(1, 5, 2, -5, 10))
print(minimum(5, 2, 4, 1, 10))

# when low limit is specified


def minimum1(*values, low_limit=0):
    values_list = (values)
    new_list = []
    for i in values_list:
        if i > low_limit:
            new_list.append(i)

    minvalue = min(new_list)
    return minvalue


print(minimum1(1, 5, 2, -5, 10))


# method 2 : combining both functions

def minimum_value(*values, low_limit=None):
    if low_limit is None:
        return min(values)
    else:
        L = [x for x in values if x > low_limit]
        return min(L)


print(minimum_value(1, 5, 2, -5, 10))
print(minimum_value(1, 5, 2, -5, 10, low_limit=0))
print(minimum_value(-25, -15, -10, 10, 25, 15, 5, low_limit=5))
