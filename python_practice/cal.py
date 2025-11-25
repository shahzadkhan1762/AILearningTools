num1=input('Enter first number :');
num2=input('Enter second number :');
op=input('Enter an operator :');
if(op=='+'):
	print('the addition is '+str(num1+num2));
if(op=='-'):
	print('the Division is '+str(num1-num2));
if(op=='*'):
	print('the multiplication is '+str(num1*num2));
if(op=='/'):
	print('the division is '+str(num1/num2));
else:
	print("please enter a valid operator");