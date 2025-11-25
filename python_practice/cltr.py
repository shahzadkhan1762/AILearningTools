num1=None;
num2=None;
result=None;
op=None;
print("(1) Addition");
print("(2) Multiplication");
print("(3) Division");
print("(4) Subtraction\n");
num1=int(input("Enter a Number : "));
op=input("Enter Operator : ");
num2=int(input("Enter Second Number : "));
if op=='+':
	result=num1+num2;
elif op=='*':
	result=num1*num2;
elif op=='/':
	result=num1/num2;
elif op=='-':
	result=num1-num2;
else:
	print("Sorry! Invalid Operator");

if result!=None:
    print(num1,op,num2," = ",result);


