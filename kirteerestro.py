#DHABA
menu = {
 'PIZZA':240,
    'PASTA':120,
    'SHAHIPANIR':150,
    'MAGGIE':100,
    'COFFE':130,
    'FRY RICE':220,
    'VEG BIRYANI':230
}
menu1={
    "CHILLY CHICEKEN":350,
    "CHICKEN FRY":300,
    "CHICKEN TANDOORI" :400,
    "CHICKEN BIRYANI":430
}
menu3={
    'PIZZA':240,
    'PASTA':120,
    'SHAHIPANIR':150,
    'MAGGIE':100,
    'COFFE':130,
    'FRY RICE':220,
    'VEG BIRYANI':230,
    "CHILLY CHICEKEN":350,
    "CHICKEN FRY":300,
    "CHICKEN TANDOORI" :400,
    "CHICKEN BIRYANI":430
}

print ("WELCOME TO KIRTEE'S RESTRO")
print("""
 VEGETARIAN ITEM 
    PIZZA :240
    PASTA :120
    SHAHIPANIR :150
    MAGGIE :100
    COFFE :130
    FRY RICE :220
    VEG BIRYANI :230
      
    NON-VEGETARIAN ITEM 
     CHILLY CHICEKEN :350
     CHICKEN FRY :300
     CHICKEN TANDOORI :400
     CHICKEN BIRYANI :430
""")
print("""what are you want to oder 
      if you want to order vegetarian item than enter 1 
      otherwise press 2 for non vegetarian item
      and if you want to order both item then press 3""")
order=int(input("Enter the order:"))
if order==1:
        num=int(input("How many item you want order :"))
        order_total=0
        for i in range(num):#3
          item1=input("Enter the name of item you want to order :")
          s=item1
          item=s.upper()
          if item in menu:
              print(f"Your item {item} has been added to your order")
              order_total+= menu[item]
          else:
             print(f" Ordered item {item} is not avaiable yet")
             print("""sorry for this inconvenience,This time we are povided this item
                            PIZZA :240
                            PASTA :120
                            SHAHIPANIR :150
                            MAGGIE :100
                            COFFE :130
                            FRY RICE :220
                            VEG BIRYANI :230""")
             item1=input("Enter the name of item you want to order :")
             s=item1
             item=s.upper()
             if item in menu:
                    if item in menu:
                     print(f"you item {item} has been added to your order")
                     order_total +=menu[item]
                    else:
                       print(f" Ordered item {item} is not avaiable yet")
                       print("""sorry for this inconvenience,This time we are povided this item
                                    PIZZA :240
                                    PASTA :120
                                    SHAHIPANIR :150
                                    MAGGIE :100
                                    COFFE :130
                                    FRY RICE :220
                                    VEG BIRYANI :230""")
        print(f"The total amount of items to pay is {order_total} ")
elif order==2:
        num=int(input("How many item you want order :"))
        order_total=0
        for i in range(num):
          item1=input("Enter the name of item you want to order :")
          s=item1
          item=s.upper()
          if item in menu1:
              print(f"Your item {item} has been added to your order")
              order_total+= menu1[item]
          else:
             print(f" Ordered item {item} is not avaiable yet")
             print("""sorry for this inconvenience,This time we are povided this item
                        CHILLY CHICEKEN :350
                        CHICKEN FRY :300
                        CHICKEN TANDOORI :400
                        CHICKEN BIRYANI :430
                                    """)
             item1=input("Enter the name of item you want to order :")
             s=item1
             item=s.upper()
             if item in menu1:
                 if item in menu1:
                  print(f"you item {item} has been added to your order")
                  order_total +=menu1[item]
                 else:
                     print(f" Ordered item {item} is not avaiable yet")
                     print("""sorry for this inconvenience,This time we are povided this item
                            CHILLY CHICEKEN :350
                            CHICKEN FRY :300
                            CHICKEN TANDOORI :400
                            CHICKEN BIRYANI :430
                                        """)
                     
        print(f"The total amount of items to pay is {order_total} ")
elif order==3:
        num=int(input("How many item you want order :"))
        order_total=0
        for i in range(num):
          item1=input("Enter the name of item you want to order :")
          s=item1
          item=s.upper()
          if item in menu3:
              print(f"Your item {item} has been added to your order")
              order_total+= menu3[item]
          else:
             print(f" Ordered item {item} is not avaiable yet")
             print("""sorry for this inconvenience,This time we are povided this item
                        VEGETARIAN ITEM 
                            PIZZA :240
                            PASTA :120
                            SHAHIPANIR :150
                            MAGGIE :100
                            COFFE :130
                            FRY RICE :220
                            VEG BIRYANI :230
      
                        NON-VEGETARIAN ITEM 
                            CHILLY CHICEKEN :350
                            CHICKEN FRY :300
                            CHICKEN TANDOORI :400
                            CHICKEN BIRYANI :430
                                        """)
             item1=input("Enter the name of item you want to order :")
             s=item1
             item=s.upper()
             if item in menu3:
                 if item in menu3:
                  print(f"you item {item} has been added to your order")
                  order_total +=menu3[item]
                 else:
                     print(f" Ordered item {item} is not avaiable yet")
                     print("""sorry for this inconvenience,This time we are povided this item
                               VEGETARIAN ITEM 
                               PIZZA :240
                               PASTA :120
                               SHAHIPANIR :150
                               MAGGIE :100
                               COFFE :130
                               FRY RICE :220
                               VEG BIRYANI :230
      
                                NON-VEGETARIAN ITEM 
                                CHILLY CHICEKEN :350
                                CHICKEN FRY :300
                                CHICKEN TANDOORI :400
                                CHICKEN BIRYANI :430
                                                """)
        print(f"The total amount of items to pay is {order_total} ")
   
else:
   print("if you want to oder something then press 1,2and 3 only")
   

