aliens=[];
for alien in range(20):
    #new_alien=;
    aliens.append({'color':'Yellow','speed':'slow','points':10});

for alien in aliens[:5]:
    print(alien);

print();

for alien in aliens[:6]:
    if alien['color']=='Yellow':
        alien['color']='red';
        alien['speed']='medium';
        alien['points']=15;


for alien in aliens[:8]:
    print(alien);
    
