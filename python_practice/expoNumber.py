base=int(input("Enter a Number : "));
exp=int(input("Enter Exponent : "));
result=1;
i=1;
for i in range(exp):
    result*=base;

print("the result is : "+str(result));