# "<", если A < B, ">", если A > B и "=", если A=B
inputs = input()
inputs2 = input()

a = int(inputs)
b = int(inputs2)

if a > b:
    print (">")
elif a < b:
    print ("<")
else: 
    print ("=")