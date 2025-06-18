class Employee:
    language = "Python"      # this is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):    # dunder method which is automatically called
       self.name = name
       self.language = language
       self.salary = salary
       print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
 
    @staticmethod
    def greet():
        print("Good morning") 
        
arpita = Employee("Arpita", "javascript", 1300000) 
# arpita.language = "java script"  # this is a object attribute
# arpita.name = "Arpita"
print(arpita.name, arpita.language, arpita.salary )

