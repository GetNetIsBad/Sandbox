#x = 1000

#for i in range(x):
#    if x % 3 == 0 or x % 5 == 0:
#        print(x)
#        x = x - 1
#    else:
#        x = x -1

a = 1
b = 2

for i in range(10):
    if a % 2 == 0:
        print(a)
    if b % 2 == 0:
        print(b)
    
    a = a + b
    b = b + a