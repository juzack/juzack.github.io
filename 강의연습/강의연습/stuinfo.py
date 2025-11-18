class Student:
    def __init__(self, name, age, average=[]):
        self.name = name
        self.age = age
        self.scores = average
        
    def add_score(self, score):
        self.scores.append(score)
        
    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
        
    def info(self):
        average_score = self.get_average
        print(f'이름: {self.name}, 나이: {self.age}, 평균점수: {average_score: .2f}')
        
        
        
    # if __name__ == "__main__":
        
# s1 = Student("ju", 17)
# s1.add_score(90)
# s1.add_score(83)
# s1.add_score(34)
    
# s1.info()
    
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
        
#     def area(self):
#         return self.width *self.height
            
#     def perimeter(self):
#         return (self.width + self.height) * 2
    
#     def is_square(self):
#         if self.width == self.height:
#             return True
#         return False

# rec1 = Rectangle(3, 3)
# rec2 = Rectangle(5, 4)

# print(f"면적: {rec1.area()}")
# print(f"둘레: {rec1.perimeter()}")
# print(f"정사각형? {rec1.is_square()}")

# print("면적: ", rec1.area())
# print("둘레: ", rec1.perimeter())
# print("정사각형? ", rec1.is_square())

# print(f"면적: {rec2.area()}")
# print(f"둘레: {rec2.perimeter()}")
# print(f"정사각형? {rec2.is_square()}")