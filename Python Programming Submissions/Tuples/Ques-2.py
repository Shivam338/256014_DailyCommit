# Write a Python program to convert a list of tuples into a dictionary

lst = [("Shivam", 256014), ("She", 256045), ("Sam", 256065)]
dic = dict()

for name, sfID in lst :
    dic.setdefault(name, []).append(sfID)
print(dic)