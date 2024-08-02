#wap to print month name according to number
num1=int(input("how many time to run this program:"))
i=0
while num1>i:
      num=int(input("Enter the  1 to 12:"))
      if num==1:
        print("january")
        break
      elif num==2:
        print("febuarry")
      elif num ==3:
        print("march")
      elif num==4:
        print("april")
      elif num==5:
        print("may")
      elif num==6:
        print("june")
      elif num==7:
        print("july")
      elif num==8:
        print("august")
      elif num==9:
        print("sepember")
      elif num==10:
        print("october")
      elif num==11:
        print("november")
      elif num==12:
         print("december")
      else:
         print("Enter valid number")
      i=i+1
