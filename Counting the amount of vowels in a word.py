#Counting the amount of vowels in a word 
#Learning to use findall

import re
def count_vowels(string):
    vowels=re.findall('[aeiou]', string, re.IGNORECASE)
    return len(vowels) #len gives the number of items in a list

string=input('Enter a word:')
print('Vowels in this word:', count_vowels(string))