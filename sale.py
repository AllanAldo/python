bill = [240 , 5000 , 22 ,1650]
total_amount = sum(bill)
print('total amount is :',total_amount)
if total_amount > 8000 :
    dis = total_amount/100 * 20
    print (dis)
    print ('distcounted bill =',total_amount-dis)
elif total_amount > 5000:
    dis = total_amount/100 * 18
    print (dis)
    print ('discounted bill =',total_amount-dis)
elif total_amount > 2000 :
    dis = total_amount/100 * 12
    print(dis)
    print('discounted bill =',total_amount-dis)