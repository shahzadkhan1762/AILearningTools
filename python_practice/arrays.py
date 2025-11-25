from array import *;

values=array('i',[4,5,63,36,3]);
print(values);
print(values.typecode);

print('****************');

for value in values:
    print(value);

print('****************');

for i in range(len(values)):
    print(values[i]);

print('*******************');

newArray=array(values.typecode,[a for a in values]);
print(newArray);
for i in range(len(newArray)):
    print(newArray[i]);


print('*****************');

newArray2=array(values.typecode, [a*a for a in values]);

for i in newArray2:
    print(i);
