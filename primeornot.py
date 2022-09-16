from re import A


def prime():
    a = int(input('enter a number :'))
    b = a
    if a > 1 :
        for i in range (2 , int(a/2 +1)):
            if (a % i) == 0:
                print(a,'is not a prime number')
            break
        else :
            print(a, 'is a prime number')
    else :
        print(a,'is not a prime number')
prime()


