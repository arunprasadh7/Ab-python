#4. Positional vs Keyword Arguments

def net_salary(basic, allowance, deduction):
    net = basic + allowance - deduction
    return  net

p = net_salary(8000, 6000, 2000)    # positional args
print(f'Net salary is {p}.')

k = net_salary(allowance=6000, deduction=2000, basic=8000) #keyword args
print(f'Net salary is Rs.{k}.')
