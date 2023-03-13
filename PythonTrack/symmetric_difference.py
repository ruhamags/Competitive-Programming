# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
A = set(list(map(int, input().split())))
M = int(input())
B = set(list(map(int, input().split())))
s_dN = A.difference(B)
s_dM = B.difference(A)
uni = s_dN.union(s_dM)
new = list(uni)

new.sort()
for i in range (len(new)):
    print(new[i])


