n =int(input("Enter the number of entries : "))
outer_list = []
for i in range(n):
    name = input("Enter Name " + str(i+1) + " : ")
    score = input("Enter Score " + str(i+1) + " : ")
    inner_list = [name, int(score)] 
    outer_list.append(inner_list)
    
print(outer_list)