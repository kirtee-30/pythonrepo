#wap to check given number is prime or not 
num=int(input("Enter the number:"))
if num==0 or num==1:
    print("not prime")
for i in range(2,num):
    if num%i==0:
        print("not prime number")
        break
    else:
        print("prime number")
        break
