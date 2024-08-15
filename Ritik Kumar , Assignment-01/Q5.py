#Create a program that checks if a given year is a leap year.
a = int(input("Enter a Year: "))
if(a % 4 == 0, a % 400 == 0):
    print("This Year is a Leap Year")

else:
    print("This is not a Leap year")