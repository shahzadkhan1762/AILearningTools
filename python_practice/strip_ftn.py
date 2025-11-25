# REMOVING WHITE SPACES FROM STRINGS
name=' waqas';
print(name);
print(name.lstrip());  # Left strip function is used to strip a string from left.

name='waqas   ';
print(name);
print(name.rstrip()); # Right strip function is used to strip a string from right

name='  waqas   ';
print(name);
print(name.strip());  # Strip function remove white spaces from both sides;

#but still name contain unstrip string
# solution
print(name);
name=name.strip();
print(name);
