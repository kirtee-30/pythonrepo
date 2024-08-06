#match case
#wap to print day name according to number
num=int(input("Enter a number:"))
match num:
    case 1:print("Monday")
    case 2:print("Tuesday")
    case 3:print("Wednesday")
    case 4:print("Thusday")
    case 5:print("Friday")
    case 6:print("Saturday")
    case 7:print("Sunday")
    case _:print("Please Enter 1 to 7")
        
