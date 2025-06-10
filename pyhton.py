def add(p,q):
    return p+q
def subract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
def modulus(p,q):
    return p//q
def power(p,q):
    return p**q
num1=int(input("enter a number of your choice:"))
num2=int(input("enter a number of your choice:"))
input1=str(input("enter if u want addition ,subraction,division,multiplication,power,modulus : "))
if  input1=="addition":
    print("num1"+"+"+"num2"+"=",add(num1,num2))
if  input1=="subraction":
    print("num1"+"-"+"num2"+"=",subract(num1,num2))
if  input1=="multiplication":
    print("num1"+"*"+"num2"+"=",multiply(num1,num2))
if  input1=="division":
    print("num1"+"/"+"num2"+"=",divide(num1,num2))
if  input1=="modulus":
    print("num1"+"//"+"num2"+"=",modulus(num1,num2))
if  input1=="power":
    print("num1"+"**"+"num2"+"=",power(num1,num2))