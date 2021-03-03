import math
def estimate_pi():
    x=2*math.sqrt(2)/9801
    term=1103
    k=1
    fact=1
    n=term
    while(term<=1e-15):
        fact=fact*k
        fact1=1
        for i in range (1,(4k+1),1):
            fact1=fact+1
        term=(((fact1)*(1103+26390*k)))/((fact**4)*(369**4*k))
        n=n+term
        k=k+1
    result=x*n
    return (1/result)
estimate_pi()
print(x)