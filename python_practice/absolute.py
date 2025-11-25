def abst(num):
    if num<0:
        return (-num);
    else:
        return num;
        
number=int(input("Enter a Number : "));
print("the absolute value of "+str(number)+" is "+str(abst(number)));