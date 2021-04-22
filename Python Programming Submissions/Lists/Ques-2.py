# Write a Python program to change the position of every n-th value with the (n+1)th in a list

lst = []
n = int(input("Enter size of List (Only Even Values numbers) : "))
if n % 2 == 0:
    for i in range(n):
        nums = int(input())
        lst.append(nums)

    for i in range(0, len(lst), 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]

    print(lst)
else:
    print("Not Possible for odd numbers !!")
    quit()

