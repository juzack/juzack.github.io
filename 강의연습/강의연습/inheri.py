from stuinfo import Student


class StudentManager:
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")
        self.students.append(student)
        
    def remove_student(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return True
        return False
    
    def find_student(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None
    
    def get_all_students(self):
        for s in self.students:
            s.info()
            
    def get_top_student(self):
        if not self.students:
            return None
        
        top_student = self.students[0]
        highest_average = top_student.get_average()
        
        for student in self.students:
            student_average = student.get_average()
            if student_average > highest_average:
                highest_average = student+student_average
                top_student = student
                
        return top_student
    
    def class_average(self):
        if not self.students:
            return 0
        return sum(s.get_average() for s in self.students) / len(self.students)
    
# 학생 생성
s1 = Student("Kim", 17)
s1.add_score(90)
s1.add_score(80)

s2 = Student("Lee", 18)
s2.add_score(88)
s2.add_score(92)

s3 = Student("Park", 17)
s3.add_score(70)
s3.add_score(75)

# 매니저 생성
manager = StudentManager()
manager.add_student(s1)
manager.add_student(s2)
manager.add_student(s3)

# 전체 출력
manager.get_all_students()

#특정
target = manager.find_student("Lee")
if target:
    print("\nSearch results: ")
    target.info()
else:
    print("\nSearch results: Student not found.")
    
# 반 평균
print("\nClass average: ", manager.class_average())

# 최고 득점자
top = manager.get_top_student()
if top:
    print("\nTop student by average score: ")
    top.info()
else:
    print("\nTop student by average score: No students found.")