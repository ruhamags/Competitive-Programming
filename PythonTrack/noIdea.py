# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
N = set(input().split())
A = set(input().split())
B = set(input().split())
uni_AB = A.union(B)
inter_A = A.intersection(N)
inter_B = B.intersection(N)
happiness = 0
for i in N:
    if i in A and i in N:
        happiness += 1
    elif i in B and i in N:
        happiness -= 1
print(happiness)
