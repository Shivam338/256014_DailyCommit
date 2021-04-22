# Write a Python program to find the repeated items of a tuple

lst = []
n = int(input("Enter Size of Tuple : "))

for i in range(n):
    nums = int(input())
    lst.append(nums)

Tup = tuple(lst)
Set = set(Tup)
finalSet = list(Set)

for i in range(len(finalSet)):
    print("Occurences of ", finalSet[i])
    count= Tup.count(finalSet[i])
    print(count)
