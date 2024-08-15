#Create a program that prints the multiplication table of a given number using a while loop.
num = int(input("Enter a number: "))
i=0
while i < 10:
    i += 1
    print(f"{num} x {i} = {num*i} ")
    