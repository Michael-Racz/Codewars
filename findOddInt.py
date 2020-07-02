'''
  Given an array, find the integer that appears an odd number of times.

  There will always be only one integer that appears an odd number of times.

'''

def find_it(seq):
    myDict = {}
    for numb in seq:
        if numb in myDict.keys():
            myDict[numb] += 1
        else:
            myDict[numb] = 1
    for kEYS,vALUE in myDict.items():
        if myDict.get(kEYS) % 2 == 1:
            print(str(myDict.get(kEYS)))
            return kEYS
    return None
    
#TESTS
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
