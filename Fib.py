from time import time

def run(func,arg):
    """
    Calculate the execution time
    """
    start = time()
    ans = func(arg)
    end = time()

    ex_time = (end-start)*1000

    print(f"{func.__name__}({arg}) take {ex_time} ms to execute")
    print(f"Output : {ans}")


#Recursive function
def re_fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return re_fib(n-1) + re_fib(n-2)

#Memorize function
def me_fib(n,dic = {}):
    if n in dic:
        return dic[n]

    if n == 0 or n == 1:
        return 1
    else:
        dic[n] = me_fib(n-1)+ me_fib(n-2)
        return dic[n]

#Tabulation function
def ta_fib(n):
    ans = {0:1,1:1}
    for i in range(2,n+1):
        ans[i] = ans[i-1]+ ans[i-2]
    return ans[n]

run(me_fib,30)
run(ta_fib,30)
run(re_fib,30)
