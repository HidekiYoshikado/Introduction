def guess_age(x):
    l=0
    s=50
    h=100
    while h-l>0:
        if x>s:
            l=s+1
        elif x<=s:
            h=s
        s=int((h+l)/2)
    return s

class Human:
    def __init__(self,x):
        self.age=x

def test():
    for i in range (1,101):
        human=Human(i)
        a=human.age
        if a==guess_age(a):
            print(str(i)+" Correct")
        else:
            print(str(i)+" False")

test()