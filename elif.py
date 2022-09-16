mark = int(input('enter you score :'))
if mark >= 80 and mark <= 100:
    print ('very good')
elif mark >= 60 and mark <= 80 :
    print ('good')
elif mark >= 40 and mark <= 60 :
    print ('just pass')
elif mark <= 40 :
    print ('failed')
else :
    print('invalid input')