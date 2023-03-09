if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    percentage = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        
        student_marks[name] = scores
        avg = sum(scores)/len(scores)
        percentage[name] = avg
        
    query_name = input()
    for key, value in percentage.items():
        if key == query_name:
            print("%.2f" %value)
    