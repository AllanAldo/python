# class A:

#     def display1(self):
#         print('display1')

    
#     def display2(self):
#         print('display1')

#     def display3(self):
#         print('display1')


# class B(A):

  
    
#     def display4(self):
#         print('hello')
    
#     def display5(self):
#         print('haiii')


# objb = B()

#second example

class car():
    def seats(self):
        print(5)

    def engine(self):
        print('ICE')

    def tyres(self):
        print(4)
   
class model(car):

    def make(self):
        print('suzuki')
     
    def engine(self):
        print('ICE')

    def color(self):
        print('black')

objcar = model()
 

