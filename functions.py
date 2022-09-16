# def prime():
#     print('hello')
# prime()

# def prime(n , m , i):
#     print(n+m+i)
# prime(6 , 5 , 3)

#  print(a+b)
# def prime():
#     a=5
#     b=10
#     print (a+b)
# prime()

# def prime(*a):
#     print('the value is', a[2])
# prime('h ', 'e', 'l', 'l' , 'o')


#keyword argument
# def prime(a , b , c):
#     print(a)
# prime(a=5 , b=3 , c=9)



# def prime(a):
#     c = ""
#     for i in a:
#         c = i + c
#     return c
# a = "allan"
# print(a)
# print(prime(a))

# def reverse(a):
#     b = ""
#     c = len(a)
#     while c > 0:
#         b += a[c-1]
#         c= c-1
#     return b
# print(reverse('allan'))

# arbitary keyword argument
# def argument(**a):
#     print( a['username'])
# argument(username = 'allan' , password = "12345")

#default parameter value
# def parameter(name='allan'):
#     print(name)
# parameter()
# parameter('aravind')

#return value
# def function(a , b):
#     return a+b
# print(function(10 , 20))

def palindrome():
   b = int(input('enter a number :'))
   c = b
   rev = 0
   while( b > 0 ):
         dig = b%10
         rev = rev*10 + dig
         b = b//10 
   if (c == rev):
        print('the entererd value is a palindrome')
   else :
        print('the enetered value is not a palindrome')
palindrome()



