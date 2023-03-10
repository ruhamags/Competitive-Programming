def swap_case(s):
    swapped = ''
    for i in s:
        if (i.isupper() == True):
            swapped += (i.lower())
            
        elif (i.islower() == True):
            swapped += (i.upper())
        else:
            swapped += i
            
    return swapped



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)