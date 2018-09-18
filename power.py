def p(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*p(base,exp-1))
base=int(input())
exp=int(input())
print(p(base,exp))
