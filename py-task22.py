import random
import os
os.system('cls')

n = int(input("Введите кол-во элементов первого набора: "))
m = int(input("Введите кол-во элементов второго набора: "))
# n = 6
# m = 7

min = 1
max = 6
nums1 = []
nums2 = []
for num in range(0,n):
    nums1.append(random.randint(min,max))
print(nums1)
for num in range(0,m):
    nums2.append(random.randint(min,max))
print(nums2)
setNum1 = set(nums1)
# print(setNum1)
setNum2 = set(nums2)
# print(setNum2)
setNew = setNum1 & setNum2
print(f"Пересечение: {setNew}")