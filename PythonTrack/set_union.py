# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
N = set(map(int, input().split()))
B = int(input())
M = set(map(int, input().split()))
uni = N.union(M)
total = 0
for i in uni:
    total += 1
print(total)
