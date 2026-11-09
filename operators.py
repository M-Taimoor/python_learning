# comparison operators
x =5
y = 7
# euality 
print(x==y)

print(x!=y)

# greater Than

print(x>y)
print(y >x)

print(x >= y)

print(y >=x)

# less than 
print(x<y)

print(x<=y)

print(y<x)

print(y<=x)


# assignment operators

x = 10
y  = 20
z =y +x
x = z

# compund assignment operators


x -=y

x =x+x
print("Value in x", x)

# logiacl operators

# and 
# or 
#not


x = 20
y = 30
and_logical  =  x and y
print(and_logical )


or_logical = x or y

print(or_logical)

not_locaical = not y

print(not_locaical)

x = 40
y =  30

print("This is the logical resutls")
print(x >y and y< x)
print(x <y and y< x)

print(x >y or y> x)

print(x <y or y< x)

print("Not operator workiing")
print(not(x >y) and y< x)

print("Not operator working")
print(not(not(x >y) and y< x))