class User:
    
    def __init__(self, name):
        self.name = name
    
    def log_in(self):
        # print("User.__init__ called.")
        self.logged_in = True
        return self.logged_in
        
        
        
class Student(User):
    
    def __init__(self, name, grade):
        # print("Student.__init__ called.")
        super().__init__(name)
        self.grade = grade
    
    def log_in(self):
        super().log_in()
        self.in_class = True
        return self.in_class
        
student1 = Student("Kimberly", 50)
# student1.log_in()
print(student1.log_in())
print(student1.__dict__)
