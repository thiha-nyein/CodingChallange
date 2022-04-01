def gcd(a):
    m =  min(a)
    while len(a)>1:
        #print(a)
        m = min(a)
        a = {i if i == m else i%m for i in a if i%m or i == m}
    #print("GCD is ",m)
    return m
  
  
def lcm(a):
  if len(a) == 1:
        return a[0]
    for i,t in enumerate(zip(a[:-1],a[1:])):
        x,y = t
        a[i+1] = x*y/gcd(t)
        print(i,x)
    print(a)
    return a[-1]
lcm([2,3,6])
