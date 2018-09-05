def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2
while(True):
    print("""1- Addition
2- substraction
3- multiply
4- division""")

    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    choice=int(input("Enter your choice: "))
    if(choice==1):
        print(add(num1,num2))
    elif(choice==2):
        print(sub(num1,num2))
    elif(choice==3):
        print(mul(num1,num2))
    elif(choice==4):
        print(div(num1,num2))


