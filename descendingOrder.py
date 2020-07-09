'''
Function takes in any number( as an integer) and makes it the largest form of the integer using the same numers.
  This is done with sorting.
'''

def descending_order(num):
    # Bust a move right here
    b = str(num)
    a = []
    for i in b:
        a.append(i)
    a.sort()
    a.reverse()
    return int(''.join(a))
