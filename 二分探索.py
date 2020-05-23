def binarysearch(s):
    l=0
    h=1000000
    while l<h:
        s=(l+h)/2
        if f(s)==0:
            return s
        if f(s)>0:
            l=s
        else:
            h=s

