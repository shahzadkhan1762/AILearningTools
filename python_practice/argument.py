def make_shirt(size,text):
	print('the size of shirt is '+size+' and text on shirt is '+text);
	
make_shirt('large','I Love pakistan');
make_shirt(size='small',text='I Love Pakistan');  
#make_shirt(size='medium','I Love Pakistan');  # does't support 

def make_shirt(size,text='I Love pakistan'):
    print(size,' shirt',' with text ',text);
    
make_shirt('large');
make_shirt('small','I Love my country');
make_shirt(size='medium');

