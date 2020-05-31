def binarysearch():
    l=0
    h=1000000
    while l<h:
        s=(l+h)/2
        def f(x):
            return 100-5*x**2/2
        mid=f(s)
        if mid==0:
            break
        if mid>0:
            l=s
        else:
            h=s
    print(str(s))

binarysearch()