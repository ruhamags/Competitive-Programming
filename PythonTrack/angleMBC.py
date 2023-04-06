# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = float(input())

BC = float(input())
tanTeta = AB/BC
teta = math.degrees(math.atan(tanTeta))

print(str(round(teta)) + u'\N{DEGREE SIGN}')
