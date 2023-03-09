if __name__ == '__main__':
    N = int(input())
    init = []
    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            init.insert(int(command[1]),int(command[2]))
        
        elif command[0] == "remove":
            init.remove(int(command[1]))
        
        elif command[0] == "append":
            init.append(int(command[1]))

        elif command[0] == "sort":
            init.sort()
        
        elif command[0] == "pop":
            init.pop()
        
        elif command[0] == "reverse":
            init.reverse()
        
        else:
            print(init)