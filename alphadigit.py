#wap to check given char is alphabet or digit or special symbol
ch=input("Enter any character:")
if ((ch>="a" and ch<="z" )or(ch>="A" and ch<="Z")):
    print("Alphabet")
elif ch>="0" and ch <="9":
    print("number")
else:
    print("specail symbole")