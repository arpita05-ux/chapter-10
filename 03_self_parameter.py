class Employee:
    language = "Python"      # this is a class attribute
    salary = 1200000


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    # def greet(self):
    #     print("Good morning")      # if i don't want to use self then we use decorator.(wi don't want any property of object)
 
    @staticmethod
    def greet():
        print("Good morning") 
        
arpita = Employee() 
arpita.language = "java script"  # this is a object attribute

arpita.getInfo()
# Employee.getInfo(arpita)
arpita.greet()
