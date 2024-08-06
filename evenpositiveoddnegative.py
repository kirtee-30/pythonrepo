#wap to check given number is even-positive or 
#or odd-negative or odd-negative.
num=int(input("Enter a number:"))
if num==0:
    print("number is zero")
else:
    if num%2==0:
        if num>0:
            print("number is even-positive")
        else:
            print("Number is even-negative")
    else:
        if num>0:
            print("number is odd-positive")
        else:
            print("number is odd-negative")