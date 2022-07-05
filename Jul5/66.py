N = input()
keybord = "qwertyuiopasdfghjklzxcvbnm"

if N == keybord[len(keybord)-1]:
    print (keybord[0])

for i in range(len(keybord)-1):

    if N == keybord[i]:
        print (keybord[i+1])

    