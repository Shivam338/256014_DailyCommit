# HackerRank Solution

for i in range(1,int(input())):
    print(int(bin(2**i-1)[2:2*i+1])*i)

# Output:
# 1
# 22
# 333
# 4444
# 55555
