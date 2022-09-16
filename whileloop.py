# i=0
# while (i<5):
#     print(i)
#     i=i+1 


password = "allan"
guess = ""
count = 1
attempt = 2
while password != guess:
    guess = input('enter password :')
    if password == guess :
        print ( 'login successfull')
        break
    else :
        count += 1
        
        if count > 3 :
            print('too many attempts')
            break

        print('login failed ', attempt, 'Attempts left')
        attempt -= 1

