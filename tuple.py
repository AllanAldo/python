num=(10, 20, 30, 40, 50, 60, 60)
print(num)

# print(num[0])
# num[0]=20
# print(num)

numList = list(num)
print(numList)
numList[0] = 23
print(numList)
num = tuple(numList)
print(num)
