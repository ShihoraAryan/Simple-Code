#write a program to swap two number without using third variable
num1=int (input("Enter Number 1:"))
num2=int (input("Enter Number 2:"))
print("Before swapping number 1",num1)
print("Before swapping number 2",num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("after sweeping number1",num1)
print("after sweeping number2",num2)
