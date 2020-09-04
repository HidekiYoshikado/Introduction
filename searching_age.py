class Human:
    def __init__(self,y):
        self.age=y
    
    def answer(self,n):
        if n<self.age:
            return "Yes"
        else:
            return "No"




def guess_age(Human):
    l=0
    s=50
    h=100
    while h-l>0:
        x=human.answer(s)
        if x=="Yes":
            l=s+1
        else:
            h=s
        s=int((h+l)/2)
    print(s)

    if s==human.age:
        print("Correct")
    else:
        print("False")

for i in range (1,101):
    human=Human(i)

    guess_age(human)