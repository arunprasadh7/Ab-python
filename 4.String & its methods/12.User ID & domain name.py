#Find user id and domain name from email address
'''
email = input("Enter email address : ")
print(email)
split_email = email.split('@')
user_name = split_email[0]
domain_name = split_email[1]
print("User Name :",user_name)
print("Domain Name :",domain_name)
'''

#method 2

emailid = input('Enter email : ')
at_rate = emailid.find('@')
#print(at_rate)
print("Username :",emailid[:at_rate])
print("Domain :",emailid[at_rate+1:])