numbers = [ 12, 20, 34, 34, 54]

for i in numbers:
    if i % 5 == 0:
        print(i)
        break
else:
    print('iteration all are completed')