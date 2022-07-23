
import re

sentence = input()
words = re.findall('[A-Z][^A-Z]*', sentence)

answer = "Yes"

if sentence[0].isupper():

    for i in range(0, len(words)):
        if len(words[i]) > 4 or len(words[i]) < 2:
            answer = "No"
else:
    answer = "No"

print(answer)
