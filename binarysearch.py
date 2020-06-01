y=10
v=6
def f(x):
    return y-4.9*(x/v)**2

#小数点移動　四捨五入
def myround(x,c):
    return (x/10**c+0.5)//1*10**c

def binarysearch():
    l=0
    h=1000000
    while h-l>0:
        s=(l+h)/2
        mid=myround(f(s),-2)
        if mid==0:
            break
        if mid>0:
            l=s
        else:
            h=s
    return myround(s,-2)
result=binarysearch()
print(result)