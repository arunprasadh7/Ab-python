#Confirming password

pass1 = input("Enter password : ")
pass2 = input("Rewrite password : ")

if pass1 == pass2:
    print("Password match")
elif pass1.lower() == pass2.lower():
    print("Rewrite using proper character case")
else:
    print("Incorrect password")