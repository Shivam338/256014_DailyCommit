# ------ 1st Program ------ #
"Hello Python"
print(__doc__)
# OutPut= Hello Python

# ------ 2nd Program ------ #
a=int(input("Enter a no."))
b=int(input("Enter a no."))
res=a+b
print(type(res))
# Output = int

# ------ 3rd Program ------ #
a=10
b=20
del a
print(a+b)
# name 'a' is not defined

# ------ 4rd Program ------ #

fval=2.3
ival=int(fval)
print(ival)

ch='A'
#ival=int(ch,10)
aval=ord(ch)
print(aval)

s1="2378"
ival=int(s1)
s2="45a64"
#ival=int(s2)

ival=23
s3=str(ival)
print(s3)

hval="23"
ival=int(hval,16)
print(ival)

s4="12.235"
fval=float(s4)

print(int(0x1D))
print(hex(45))
print(oct(0o23))
print(bin(13))
print(int(0b11011))
# Output= 2,65,23,35,29,0x2d,0o23,0b1101,27

# ------ 5th Program ------ #
x=10
y=2.3
s1="hello"
ch='A'
flag=True
c1=2+3j
print(type(c1))
# similarly check type of others
print(isinstance(x,int))
# Output = <class 'complex'>, True

# ------ 6th Program ------ #

a=32
b=10
c=a/b
d=a//b
print(c,d)
x=2
y=5
z=x**y
# q=x(y-5) This statement gives error
q=x*(y-5)
x+=5
# Output = 3.2  3

# ------ 7th Program ------ #
a=10
b=2
c=0
print(a and b)
print(b and a)
print(a and c)
print(c and b)
print(a or b)
print(b or a)
print(a or c)
print(c or b)
# Output= 10,2,10,2

# ------ 7th Program ------ #
s1="Hello"
s2="Hello"
ch='e'
c2='x'
print(s1==s2)
print(s1 is s2)
print(ch in s1)
print(c2 not in s2)
# OutPut= All are true

# ------ 8th Program ------ #
xval = -12.785
print(abs(xval))
print(round(xval,2))
# Output = 12.785, -12.79

# ------ 9th Program ------ #
a,b=10,20
a,b=b,a
print(a,b)
# Output = 20,10

# ------ 10th Program ------ #
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)
# OutPut = 20, 10