s = input()
length = len(s)
count = 0

for i in range(length-4):
    if s[i]=='>':
        if s[i+1]=='>':
            if s[i+2]=='-':
                if s[i+3]=='-':
                    if s[i+4]=='>': 
                        count+=1 

for i in range(length-4):
    if s[i]=='<':
        if s[i+1]=='-':
            if s[i+2]=='-':
                if s[i+3]=='<':
                    if s[i+4]=='<': 
                        count+=1 

print(count)