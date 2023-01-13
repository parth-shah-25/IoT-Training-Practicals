a,b = 5,3

print("Arithmetic Operators--------")
print("Addition: ",a+b)
print("Substraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Modulo: ",a%b)
print("Power: ",a**b)

print("Assignment Operators--------")
a+=2
print("Addition Assignment: ",a)
a-=2
print("Subtraction Assignment: ",a)
a*=2
print("Multiplication Assignment: ",a)
a/=2
print("Division Assignment: ",a)
a%=2
print("Reminder Assignment: ",a)
a**=2
print("Exponent Assignment: ",a)

print("Comparison Operators-----")

print("Is Equal to: ",a==b)
print("Not Equal to: ",a!=b)
print("Greater Than: ",a>b)
print("Less Than: ",a<b)
print("Greater Than or Equal to: ",a>=b)
print("Less Than or Equal to: ",a<=b)

print("Identity Operators-------------")
print(a is b)

list1,list2=[1,2,3],[1,2,3]
print(list1 is list2)

print('Membership Operators-----------')
msg = "This is a message"
dict1 = {1:'a',
         2:'b'}

# print('x' not in msg)
print('x' in msg)
print(1 in dict1)