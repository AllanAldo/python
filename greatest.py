def prime(a , b , c):
# a = int(input ('enter value of a :'))
# b = int(input('enter value of b :'))
# c = int(input('enter value of c :'))
# if a > b and a > c :
#     print(a, ' is the greatest number')
# elif b > a and b > c :
#     print(b, 'is the greatest number')
# else :
#     print(c, ' is the greatest number')

    if a > b:
        if a > c:
            print('greates is ', a)
        else:
            print('greates is ', c)
    elif b > c:
        print('greates is ', b)
    else:
        print('greates is ', c)

prime( 4 , 6 , 10)
