a = int(input())
b = int(input())
c = int(input())

if a<b:
    if a<c: # a is smallest
        if b<c: 
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if b<c: # b>a
        if a<c:
            print(b,a,c)
        else: #c>a
            (b,c,a)
    else: # c>b
        print(c,b,a)
        