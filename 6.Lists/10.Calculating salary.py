#Calculating salary challenge
#Calculate salary, weekly working hours in a given list

work_hours = [int(x) for x in input('Enter work hour per day in a week,seperated by space : ').split()]
total_work_hours = sum(work_hours)
print('Total work hour\'s is :',total_work_hours,'hr')
hourly_wage = int(input('Enter hourly wage : '))

salary = total_work_hours * hourly_wage
print('Your weekly salary is :',salary + '$')
