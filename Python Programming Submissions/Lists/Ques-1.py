# Write a Python program to find the second smallest number in a list

lst = []
n = int(input("Enter size of List : "))

for i in range(n):
    nums = int(input())
    lst.append(nums)

length = len(lst)
lst.sort()
print("Second Largest element is:", lst[length - 2])