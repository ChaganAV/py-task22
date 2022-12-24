def FindIntersect(set1, set2):
    nums = []
    for num in set1:
        if num in set2:
            nums.append(num)
    return nums