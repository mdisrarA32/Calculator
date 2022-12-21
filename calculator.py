num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))

print("enter 1 for 'addition' \n enter 2 for subtraction \n enter 3 for multiplication \n enter 4 for division \n enter 5 for modulous ")

Enter_number=int(input("choose a number from 1 to 8: "))

if Enter_number == 1:
    print("addition of two number: ",num1+num2)

if Enter_number ==2:
    print("subtraction of two number: ",num1-num2)

if Enter_number == 3:
    print("multiplication of two number : ",num1*num2)

if Enter_number == 4:
    print("Division of two number : ",num1/num2)

if Enter_number == 5:
    print("modulous of two number: ",num1//num2)


