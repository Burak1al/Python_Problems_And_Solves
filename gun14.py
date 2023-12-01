# def solve(name):
#     words = name.split()
#     capitalizedletter = ''
#     for word in words:
#         capitalizedletter += word.lower().capitalize() + ' '
#     return capitalizedletter
#
# if __name__ == '__main__':
#     name = input()
#     print(solve(name))
# def solve(name):
#     words = name.split()
#     capitalized_letter = ''
#     for word in words:
#         capitalized_letter += word.lower().capitalize() + ' '
#     return capitalized_letter.strip()
#
# if __name__ == '__main__':
#     name = input("Enter a name: ").strip()
#     print(solve(name))
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    capitalized_name = ' '.join(word.capitalize() for word in s.split())
    return capitalized_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') if 'OUTPUT_PATH' in os.environ else sys.stdout

    s = input().strip()

    result = solve(s)

    fptr.write(result + '\n')

    if fptr != sys.stdout:
        fptr.close()
#HACKERRANK UYUZ ETTİ BASİT AMA TEKRAR YAZMAYA ÜŞENDİM YAPMIŞIM GİBİ DAVRAN