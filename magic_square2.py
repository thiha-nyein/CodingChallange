N = int(input("Enter Odd number: "))
mid = N-1
pad = N//2

def cor(x):
    if x < pad:
        return x+N
    elif x > mid+pad:
        return x-N
    else:
        return x

for r in range(N):
    line = []
    for c in range(N):
        row = mid+r-c
        col = r+c

        if row != col or row+col != 2*mid:
            row = cor(row,N)
            col = cor(col,N) 

        row = row - pad
        col = col - pad
        
        line.append(str(row*N + col+1).rjust(3," "))
    print("|".join(line))


