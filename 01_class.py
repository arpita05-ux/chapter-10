class Employee:
    language = "Py"      # this is a class attribute
    salary = 1200000

arpita = Employee() 
arpita.name = "Arpita"  # this is a object attribute
print( arpita.name, arpita.language, arpita.salary)

ridhi = Employee()
ridhi.name = "Ridhima"
print(ridhi.name, ridhi.salary, ridhi.language)

# Here name is object attribute and 
# salary and language are class attributes as they directly belong to the class