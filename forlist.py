#wap to check negative number present in list or not
list=[12,34,-56,12,78,90]
negative=False
for i in list:
    if i<0:
        negative=True
        break
if negative:
    print("Negative number in list")
else:
    print("Not present negative number")

