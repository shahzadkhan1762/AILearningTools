visitPlaces= ['turkey','england','switzerland','dubai','suadi arabia']

print("\nVisit Places in origional Order");
print(visitPlaces);

print("\nSorted alphbaticaly Using sorted method");
print(sorted(visitPlaces));

print("\nPrint visit Places to check that it is in orgional order");
print(visitPlaces);

#print(sorted(visitPlaces(reverse=True)));
#print(visitPlaces);

print("\nVisit Places in reverse Order");
visitPlaces.reverse();
print(visitPlaces);

print("\nVisit Places Afer using reverse again");
visitPlaces.reverse();
print(visitPlaces);

print("\nVisit Places Using sort method");
visitPlaces.sort();
print(visitPlaces);

print("\nVisit Places Using sort method and set reverse=True");
visitPlaces.sort(reverse=True);
print(visitPlaces);
