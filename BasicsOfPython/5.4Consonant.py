alpa='qwertyuiopasdfghjklzxcvbnm'
print(len(alpa))
vowel='aeiou'
str="this is the sample string"

char=''

for ch in str:
    if(ch not in vowel and ch in alpa):
        char=char+ch
print(char)