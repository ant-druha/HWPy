__author__ = 'Andrey.Dernov'

def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y+ a

print(add(1,2))
print(addFixedValue(1))

# This is a text
s= "Lars"
# This is an integer
x = 1
y=4
z=x+y

#assert(1==2)

i = 1
for i in range(1, 10):
    if i <= 5 :
        print('Smaller or equal then 5.\n', end=' ')
    else:
        print('Larger then 5.\n', )

s = "abcdefg"
assert (s[0:4]=="abcd")
assert (s[4:]=="efg")
assert ("abcdefg"[4:0]=="")
assert ("abcdefg"[0:2]=="ab")

print ('this is a text plus a number ' + str(10))
