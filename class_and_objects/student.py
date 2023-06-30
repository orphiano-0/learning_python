class student:
    def __init__(self, stud_num, name, dept, gpa):
        self.stud_num = stud_num
        self.name = name
        self.dept = dept
        self.gpa = gpa
    def honors(self):
        if self.gpa <= 1.5:
            return True
        else:
            return False
