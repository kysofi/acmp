N = int(input())

surnames = []
names = []
classes = []
birthday = []

for i in range (N):
    surnames.append(input())
    names.append(input())
    classes.append(input())
    birthday.append(input())

pupils = []
pupil = []

for i in range (N):
    pupil.append(surnames[i])
    pupil.append(names[i])
    pupil.append(int(classes[i][:-1]))
    pupil.append(classes[i][-1])
    pupil.append(birthday[i])
    pupils.append(pupil)
    pupil = []

# We have now an array with pupils. Can do sorting 

# Sorting with classes numbers 

for run in range (N-1):
    for i in range (N-1-run):
        if pupils[i][2] > pupils[i+1][2]:
            pupils[i], pupils[i+1]=pupils[i+1],pupils[i]

# Sorting with classes letters
 
for run in range (N-1):
    for i in range (N-1-run):
        if pupils[i][2] == pupils[i+1][2]:
            if pupils[i][3] > pupils[i+1][3]:
                pupils[i], pupils[i+1]=pupils[i+1],pupils[i]

# Sorting with the surnames 

for run in range (N-1):
    for i in range (N-1-run):
        if pupils[i][2] == pupils[i+1][2]:
            if pupils[i][3] == pupils[i+1][3]:
                if pupils[i][0] > pupils[i+1][0]:
                    pupils[i], pupils[i+1]=pupils[i+1],pupils[i]

for i in range (N):
    print (str(pupils[i][2])+pupils[i][3], pupils[i][0], pupils[i][1], pupils[i][4])