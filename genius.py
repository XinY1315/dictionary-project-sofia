""" def christmas_trees(n, h):
    increasing_1 = 0
    decreasing_1 = 0
    increasing_2 = 0
    decreasing_2 = 0
    for i in range(n):
        if i % 2 == 0:
            if n[i] < n[i+1]:
                increasing_1 += 1
            else:
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
            print(decreasing_1) """


def trees(n, h):
    n = range(2, 2000)
    current_increasing = 1
    current_decreasing = 1
    best_increasing = 0
    best_decreasing = 0
    for i in range(n-1):
        if h[i] > h[i+1]:
            current_decreasing += 1
            if current_decreasing > best_decreasing:
                best_decreasing = current_decreasing
        elif h[i] < h[i+1]:
            current_decreasing == 0
            current_increasing += 1
            if current_increasing > best_increasing:
                best_increasing = current_increasing
        else:
            current_increasing = 1
            current_decreasing = 1
h = [1, 3, 5, 2]
trees([1,2,3,4,5], h)