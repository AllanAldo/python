def prime():
    a = int(input('enter a number :'))
    b = 1
    for i in range(1 , a+1):
        b = b * i
    print('factorial of ',a ,'is',b)
# prime()