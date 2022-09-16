class Opearator:

    def Add(self,input1,input2):

        if(type(input1) == str and type(input2) == str):
            print('appending strings')
        
        elif (type(input1) == int and type(input2) == int):
            print('adding integers')

        else :
            print('invalid input')
    
    

op = Opearator()
op.Add('a','b')
op.Add(10,30)
