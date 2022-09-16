import json 

# a = {
#     "Name" : "Allan" ,
#     "number" : 8089594336 ,
#     # "male" : True ,
#     # "address" : {
#     #     "house name" : "ottaplakkal" ,
#     #     "street" : "vellimadukunnu"
#     # }
# }
# json.dumps(a)

# dump
# with open('dump.json','w') as dump :
#     json.dump(a,dump)


# loads
# b = json.loads(a)
# print(b['number'])

# a='{"name":"allan","age":22}'

# b = json.loads(a)
# print(b['age'])

with open('dump.json','r') as load :
    b = json.load(load)
print(b)