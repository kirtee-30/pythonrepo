#match case
#wap to print word according to number
num=int(input("How many time to run this program:"))
i=0
while i<num:
    num1=int(input("Enter the number:"))
    match num1:
        case 1:print("One")
        case 2:print("Two")
        case 3:print("Three")
        case 4:print("four")
        case 5:print("five")
        case 6:print("six")
        case 7:print("seven")
        case 8:print("eight")
        case 9:print("nine")
        case 10:print("Ten")
        case _:print("Please enter the 1 to 10 number")
    i=i+1    
