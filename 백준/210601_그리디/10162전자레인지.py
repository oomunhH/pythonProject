time=int(input())
a,b=divmod(time,300)
c,d=divmod(b,60)
e,f=divmod(d,10)
if not f==0:
    print(-1)
else:
    print("{0} {1} {2}".format(a,c,e))