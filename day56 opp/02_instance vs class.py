class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000


shubham= Employee()
shubham.language = "JavaScript" # This is an instance attribute
print(shubham.language, shubham.salary)