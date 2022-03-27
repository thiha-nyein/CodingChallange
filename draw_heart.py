#Mar 27 2022 06:54
#For MyoPaPaKyaw
#V:1

n = int(input("Input number: "))

print(f"Total Row: {3*n-2}\nMaximun number of star: {4*n-3}")
#total row = 3*n-2
#max_star = 4*n-3
for row in range(3*n-2):
    if row < n:
        space = " " * (n-row-1)
        stars = "*" * (2*row+1)
        line = space + stars + space
        print(line+line[1:])
    else:
        space = " " * (row-n+1)
        stars = "*" * (6*n-5-2*row)
        line = space + stars
        print(line)
