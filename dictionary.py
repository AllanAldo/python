# this is a python dictioanary




from unicodedata import name


userdetails = {
    'name':'allan', 
    'age': 24, 
    'qualification': 'btech',
}
print(userdetails)
print(userdetails['name'])
print(userdetails['qualification'])
userdetails['place']='kozhikode'
print(userdetails)

# userdetails.clear()
# print(userdetails)

# cpy = userdetails.copy()
# print(cpy)

# seq = ('sex', 'mail')
# userdetails = dict.fromkeys(seq)
# print(userdetails)

# print(userdetails.get('nam', 'no name'))

# print(userdetails.items())
# print(userdetails.keys())
# print(userdetails.values())
# # print(userdetails.has_key('name'))

# print(userdetails.setdefault('age','no age'))

# print(userdetails)

useraddress = {
    'house number':418,
    'place': 'kozhikodee',
    'street name':'vellimadukunu',
    
    
}

userdetails.update(useraddress)
print(userdetails)

# del useraddress
# print(useraddress)

del userdetails['age']
print(userdetails)