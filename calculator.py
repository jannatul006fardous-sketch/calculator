print("Happy Calculation!")
n1 = float(input("Enter number: "))
n2= float(input("Enter number: "))
operator= input("Enter input: ")
result= "None"
if operator =="+":
    result= n1+n2
    print(result)
elif operator== "-":
    result=n1-n2
    print(result)
elif operator =="*":
    result= n1*n2
    print(result)
elif operator=="/":
    result = n1/n2
    print(result)
else: 
      print(result)