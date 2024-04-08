import math

inp_file = open('input.txt')
a = float(inp_file.readline())
b = float(inp_file.readline())
c = float(inp_file.readline())
d = float(inp_file.readline())
e = float(inp_file.readline())
f = float(inp_file.readline())

if a==b==c==d==e==f==0:
    print(5)
elif ((a==b==0) and (e!=0)) or ((c==d==0) and (f!=0)):
    print(0)
elif (a==b==e==0):
    if (c==0):
        print(4, f/d)
    elif (d==0):
        print(3, f/c)
    else:
        print(1, -c/d, f/d)
elif (c==d==f==0):
    if (a==0):
        print(4, e/b)
    elif (b==0):
        print(3, e/a)
    else:
        print(1, -a/b, e/b)
elif (a==0):
    if (c==0):
        y1=e/b
        y2=f/d
        if y1==y2:
            print(4, y1)
        else:
            print(0)
    else:
        y=e/b
        x=(f-d*e/b)/c
        print(2, x, y)
elif (b==0):
    if (d==0):
        x1=e/a
        x2=f/c
        if x1==x2:
            print(3, x1)
        else:
            print(0)
    else:
        x=e/a
        y=(f-c*e/a)/d
        print(2, x, y)
elif (c==0):
    y=f/d
    x=(e-b*f/d)/a
    print(2, x, y)
elif (d==0):
    x=f/c
    y=(e-a*f/c)/b
    print(2, x, y)
elif (c/a == d/b):
    if f == e*c/a:
        print(1, -a/b, e/b)
    else:
        print(0)
else:
    divider = b*c-a*d
    if divider != 0:
        y=(c*e-a*f)/divider
        x=(e-b*y)/a
        print(2, x, y)
    else:
        if (e == 0):
            print(1, (c-a)/(b-d), 0)
        else:
            print(0)