

def christmas_trees(n):
    increasing_1 = 0
    decreasing_1 = 0
    increasing_2 = 0
    decreasing_2 = 0
    for i in range(n):
        if i % 2 == 0:
            if n[i] < n[i+1]:
                increasing_1 += 1
            elif n[i] <= n[i+1]:
                decreasing_1 += 1
        else:
            if n[i] > n[i+1]:
                increasing_2 += 1
            else:
                decreasing_2 += 1
            if increasing_2 > increasing_1:
                increasing_1 = increasing_2
            if decreasing_2 > decreasing_1:
                decreasing_1 = decreasing_2
            print(increasing_1)
            print(decreasing_1)
christmas_trees([1, 2, 3, 4, 5, 2, 3, 4, 1])