active=True;
while active:
    print('enter 0 to exit');
    age=int(input("what's your age : "));
    if age==0:
        print('Quit');
        break;
    elif age<3:
        print('your ticket is free');
    elif age<12:
        print('your ticket price is $10');
    else:
        print('your ticket price is $15');

    
