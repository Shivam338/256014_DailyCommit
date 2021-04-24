# Hackerrank Solution
def print_formatted(number):
    # your code goes here
    width = len(str(bin(number))[2:])
    for _ in range(1, number+1):
        print(str(_).rjust(width, ' '), str(oct(_))[2:].rjust(width, ' '), str(hex(_).upper())[2:].rjust(width, ' '), str(bin(_))[2:].rjust(width, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)