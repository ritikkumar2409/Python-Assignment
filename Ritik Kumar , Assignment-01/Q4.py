#Write a Python program that takes an integer input from the user and prints whether the number is
#positive, negative, or zero.

a = int(input("Enter a number: "))
if(a>0):
    print("Positive number")
elif(a<0):
    print("Negative number")
else:
    print("Zero number")