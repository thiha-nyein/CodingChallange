from math import gcd
from time import time

def run(func,a,b):
	start = time()
	ans = func(a,b)
	end = time()
	
	ex_time = (end-start)*1000
	print(f"{func.__name__} take {ex_time} ms to execute")
	print("Output :", ans)

#Recursion
def re_gcd(a,b):
	if b:
		return re_gcd(b,a%b)
	else:
		return a

#Euclidean Algorithm
def eu_gcd(a,b):
	while(b):
		a, b = b, a%b
	return a

#Eulidean Algorithm
run(eu_gcd,255,100)

# math module
run(gcd,255,100)

# Recursion
run(re_gcd,255,100)

mylist = [81,132,405,99]
def m_gcd(a):
    while len(a)>1:
        print(a)
        ans = set()
        m = min(a)
        for i in a:
            if i==m:
                ans.add(i)
            if i%m:
                ans.add(i%m)
        a = ans.copy()
    return a

m_gcd(mylist)
