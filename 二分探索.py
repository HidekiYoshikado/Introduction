def binarysearch(s):
    s=50
    l=0
    h=100
    while l<h:
        print("it is higher than "+str(s)+"?" )
        x=input()
        if x=="Yes":
            l=s+1
        else:
            h=s
        s=int((l+h)/2)
    return s
