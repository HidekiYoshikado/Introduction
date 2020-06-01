def myround(x,c):
    return ((x/10**c+0.5)//1)*10**c
result=myround(99.14,-1)
print(result)