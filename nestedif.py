uname = 'allanaldo'
password = '12345'
name = input('enetr your uname :')
passw = input('enter your password :')

if uname == name :
    if passw == password :
        print('login succesfull')
    else :
        print('incorrect password')
else :
    print('invalid username')