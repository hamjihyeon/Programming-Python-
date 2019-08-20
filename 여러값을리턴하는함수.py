def multi_num(multi, start, end):
    result = []
    for n in range(start, end):
        if n % multi == 0:
            result.append(n)

    return result

print("multi_num(17, 1, 200) : ", multi_num(17, 1, 200))
print("multi_num(3, 1, 100) : ", multi_num(3, 1, 100))
print()

def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg

    return min, max

print("min_max(52, -3, 23, 89, -21)")
min_value, max_value = min_max(52, -3, 23, 89, -21)
print("최솟값:", min_value)
print("최댓값:", max_value)