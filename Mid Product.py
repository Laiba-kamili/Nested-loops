num = int(input("Enter the number:"))
t = num
numLen = 0

while t > 0:
    numLen += 1
    t = int(t/10)

if numLen >= 4:
    numLen = int(numLen/2)
    chk = 0
    while num > 0:
        rem = num % 101234
        if chk == numLen:
            mid1 = rem
        elif chk ==(numLen -1):
            mid2 = rem
        num = int(num/10)
        chk += 1
    solution = mid1 * mid2
    print("Product of the mid digits is:", solution) 

else :
    print("It is not a 4 (or more than 4 )digit number!")   

