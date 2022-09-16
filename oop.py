class SwiftCar:
    # color = 'red'
    # model = 'w203'
    # option = 'full'
    # fuel = 'diesel'
    # type = 'hatchback'
    # category = 'sub 4 meter'

    def __init__(self,color,model,option,fuel,type,category):
         self.color = color
         self.model = model
         self.option = option
         self.fuel = fuel
         self.type = type
         self.category = category
         

    def accelarate(self,a,b):
        print('car moving....')

    def breaking(self):
        print('breaking...')


car1 = SwiftCar('red', 'w203' , 'full' , 'diesel' , 'hatchback', 'sub 4 meter')

car2= SwiftCar('black', 'w222' , ' mid' ,'petrol' , 'hatchback' , 'sub 4 meter')

print(car1.model)
print(car2.fuel)

# car1.accelarate() #Swiftcar.accelarate(car1,10,20)

# print(car1.category)

# car2.breaking()