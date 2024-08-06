#match case
#calculator
print(""" Welcom to our calculator
press 1 for addition
press 2 for substraction
press 3 for multiplication
press 4 for division
press 5 for modulus
press 6 for power """)
num=int(input("How many time to run this program:"))
i=0
while i<num:
    num1=int(input("what  are you want to perform action:"))
    a=eval(input("Enter the number:"))
    b=eval(input("Enter the number:"))
    match num1:
        case 1:
            sum=a+b
            print("sum of a and b:",sum)
        case 2:
            if a>b:
                sub=a-b
                print("substraction of a and b is :",sub)
            else:
                print("substraction of a and b is :",b-a)
        case 3:
            mul=a*b
            print("multiplication of a and b is:",mul)
        case 4:
            if a>b:
                print("division:",a/b)
            else:
                print("division:",b/a)
        case 5:
            if a>b:
                print("modulus:",a%b)
            else:
                print("modulus:",b%a)
        case 6:
            power=a**b
            print("Power:",power)
    i=i+1    
        


