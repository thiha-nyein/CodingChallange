# to solve the tower of honi puzzle
# feb 1 2022
def tower(n,source, temp, goal):
    if n == 1:
        print(f"move {n} disk form {source} to {goal}")
        return
    # Move (n-1) disk form source to temp
    tower(n-1,source, goal , temp)
    # Move (n ) th disk form source to goal
    print(f"move {n} disk form {source} to {goal}")

    # Move (n-1) disk form temp to goal
    tower(n-1,temp, source , goal)
tower(4,'A','B','C')
