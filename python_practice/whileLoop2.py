number = 1;
while number <5:
    print(number);
    number+=1;



prompt="\ntell me something i will repeat it for you";
prompt+="\nEnter Quite to exit : ";

message='';
while message != "Quite":
    message=input(prompt);
    print(message);




active = True;
while active:
    message = input("\n\nEnter a Message : ");
    if message == 'Quite':
        active = False;
    else:
        print(message);
        

