num1 = int(input("Enter a number here : "))
num2 = int(input("Enter another number here : "))

print("Select a function : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


a = input("Enter 1, 2, 3 or 4 : ")

if a == "1":
    print(add(num1,num2))
elif a == "2":
    print(sub(num1,num2))
elif a == "3":
    print(multi(num1,num2))
elif a == "4":
    print(div(num1,num2))
else:
    print("What the hell are you doing.")






