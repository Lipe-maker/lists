class person:
    head =1
    legs = 2
    hands =2


    def _init_(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height



    def details(self):
         print('My name is ', self.name)               
         print('I am 'self.age,'years old and ',self.height,'meters of height.')


    def modify(self):
        new_name = input('Enter a new name:')
        self.name = new_name
        new.age = int(input('Enter a age:'))
        self = new_age


p1 = person('Danstan,25,1.75')
p2 = person('DIO,116,1.8')
p3 = person('Felipe,11,1.60')
  

p1.modify()
p2.details()
