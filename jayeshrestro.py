#for loop se order


menu = {
    'PIZZA':60,
    'PASTA':120,
    'SHAHIPANIR':150,
    'MAGGIE':50,
    'COFFE':60,
}
print ("Well come to JAYESH KA DHABA ")
print("PIZZA: 60\nPASTA: 120\nSHAHIPANIR: 150\nMAGGIE: 50\nCOFFE: 60")  

num=int(input("How many item you want order : "))
order_total=0
for i in range(num):
   item=input("Enter the name of item you want to order : ")
   if item in menu:
      order_total += menu[item]
      print(f"Your item {item} has been added to your order")
   else:
      print(f" Ordered item {item} is not avaiable yet")
print(f"The total amount of items to pay is {order_total} ")