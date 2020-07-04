'''
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

    Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    Every smiling face must have a smiling mouth that should be marked with either ) or D

No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

More Examples-
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
'''
import re
def count_smileys(arr):
    smileCount = 0
    smileyMatch = re.compile(r'''(
        (\W)*
        [;|:]{1}
        [-|~]?
        [)|D]{1}
    )''',re.VERBOSE)
     #the number of valid smiley faces in array/list
    for object in arr:    
        foundSmiles = smileyMatch.search(object)
        if foundSmiles != None:
            smileCount += 1
    return smileCount
            
print(count_smileys([])) #Should return 0 when list is blank
print(count_smileys([':D',':~)',';~D',':)'])) #SHould return 4
print(count_smileys([':)',':(',':D',':O',':;'])) #should return 2
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))#Should return 1
