# Write a Python program to find maximum and the minimum value in a set

lst = []
n = int(input("Enter size of set : "))

for i in range(n):
    nums = int(input())
    lst.append(nums)

S = set(lst)
print("Maximum value in the set is = ", max(S))
print("Minimum value in the set is = ", min(S))
